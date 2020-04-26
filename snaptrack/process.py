from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from snaptrack.auth import login_required
from snaptrack.db import get_db

bp = Blueprint('process', __name__)

@bp.route('/')
def index():
	db = get_db()
	pics = db.execute (
		'SELECT p.id, author_id, created, img_path'
		' FROM img p JOIN user u on p.author_id = u.id'
		' ORDER BY created DESC' 
	).fetchall()
	return render_template('images/index.html', pics=pics)

@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():
	if request.method == 'POST':
		title = request.form['title']
		pic = request.form['photo']
		error = None

		if not title:
			error = 'Title is required.'

		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'INSERT INTO img (title, author_id}'
				' VALUES (?, ?, ?)',
				(title, g.user['id'])
			)
			db.commit()
			return redirect(url_for('process.index'))
	return render_template('process/upload.html')


