import functools
import os
import json
import sqlite3
from flask_login import (
	LoginManager,
	current_user,
	login_required,
	login_user,
	logout_user,
)
from flask import (
	Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from oauthlib.oauth2 import WebApplicationClient
import requests
# Internal imports
from snaptracks.db import init_db_command
from snaptracks.user import User
from snaptracks.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
	"https://accounts.google.com/.well-known/openid-configuration"
)
login_manager = LoginManager()
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
	return requests.get(GOOGLE_DISCOVERY_URL).json()

@bp.route('/login',methods=['GET','POST'])
def login():
	# Find out what URL to hit for Google login
	google_provider_cfg = get_google_provider_cfg()
	authorization_endpoint = google_provider_cfg["authorization_endpoint"]

	# Use library to construct the request for Google login and provide
	# scopes that let you retrieve user's profile from Google
	request_uri = client.prepare_request_uri(
		authorization_endpoint,
		redirect_uri=request.base_url + "/callback",
		scope=["openid", "email", "profile"],
	)
	return redirect(request_uri)

@bp.route('/login/callback', methods=['POST', 'GET'])
def callback():
	# Get authorization code Google sent back to you
	code = request.args.get("code")

# Find out what URL to hit to get tokens that allow you to ask for
# things on behalf of a user
	google_provider_cfg = get_google_provider_cfg()
	token_endpoint = google_provider_cfg["token_endpoint"]

	token_url, headers, body = client.prepare_token_request(
		token_endpoint,
		authorization_response=request.url,
		redirect_url=request.base_url,
		code=code
	)
	token_response = requests.post(
		token_url,
		headers=headers,
		data=body,
		auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
	)

	# Parse the tokens!
	client.parse_request_body_response(json.dumps(token_response.json()))
	userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
	uri, headers, body = client.add_token(userinfo_endpoint)
	userinfo_response = requests.get(uri, headers=headers, data=body)
	if userinfo_response.json().get("email_verified"):
		unique_id = userinfo_response.json()["sub"]
		users_email = userinfo_response.json()["email"]
		picture = userinfo_response.json()["picture"]
		users_name = userinfo_response.json()["given_name"]
	else:
		return "User email not available or not verified by Google.", 400
	user = User(
		id_=unique_id, name=users_name, email=users_email, profile_pic=picture
	)

	# Doesn't exist? Add it to the database.
	if not User.get(unique_id):
		User.create(unique_id, users_name, users_email, picture)

	# Begin user session by logging the user in
	login_user(user)
	db = get_db()	
	user = db.execute (
		'SELECT * FROM user WHERE name = ?', (users_name,)
	).fetchone()
	session['user_id'] = user['name']
	# Send user back to homepage
	return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
	user_id = session.get('user_id')
	print(user_id)
	if user_id is None:
		g.user = user_id
	else:
		g.user = get_db().execute(
			'SELECT name FROM user WHERE name = ?', (user_id,)
		).fetchone()

@bp.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

@bp.route("/handleUpload", methods=['POST'])
def fileUpload():
	if 'photo' in request.files:
		photo = request.files['photo']
		if photo.filename != '':
			photo.save(os.path.join('/home/jason/Documents/JH/projects/411/prototype/files', photo.filename))
	return redirect(url_for('index'))

def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.user is None:
			return redirect(url_for('auth.login'))
		return view(**kwargs)
	return wrapped_view
