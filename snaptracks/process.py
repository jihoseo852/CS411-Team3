import os
import hashlib
from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from snaptracks.auth import login_required
from snaptracks.db import get_db

bp = Blueprint('process', __name__)

@bp.route('/')
def index():
	db = get_db()
	pics = db.execute (
		'SELECT p.id, author_id, created'
		' FROM img p JOIN user u on p.author_id = u.id'
		' ORDER BY created DESC' 
	).fetchall()
	return render_template('images/index.html', pics=pics)

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
	if request.method == 'POST':
		title = request.form['title']	
		if 'photo' in request.files:
			photo = request.files['photo']
			print('hits here')
			if photo.filename != '':
				# doesn't work without full filepath
				photo_db_path = '/home/jason/Documents/JH/projects/411/snaptracks/photodb/'
				photo.save(os.path.join(photo_db_path, photo.filename))
				img_file = open(path).read()
				
				
		error = None

		print('hits')
		if not title:
			error = 'Title is required.'
		
		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'INSERT INTO img (title, author_id)'
				' VALUES (?, ?)',
				(title, g.user['id'])
			)
			db.commit()
			return redirect(url_for('process.index'))
	return render_template('process/upload.html')


