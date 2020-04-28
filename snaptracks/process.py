import os
import hashlib
from . import visionwithspotify
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
			if photo.filename != '':
				# doesn't work without full filepath
				photo_db_path = '/home/jason/Documents/JH/projects/411/snaptracks/photodb'
				#photo_db_path = r'C:\Users\jtayb\Desktop\CS411-Team3-master\snaptracks\photodb'
				photo_path = os.path.join(photo_db_path, photo.filename)
				photo.save(photo_path)
				with open(photo_path, 'rb') as f:
					img_file = f.read()
				md5_hash = hashlib.md5(img_file).hexdigest()
				db = get_db()
				if db.execute (
					'SELECT hash FROM img WHERE hash = ?', (md5_hash,)
				).fetchone() is not None:
					cache = db.execute(
						'SELECT body FROM img WHERE hash = ?', (md5_hash,)
					).fetchone()
					songs = cache[0]
					return render_template('process/upload.html',songs=songs)
				else:
					songs = str(visionwithspotify.process(photo_path)).strip('[]')
					return render_template('process/upload.html',songs=songs)
				
		error = None

		if not title:
			error = 'Title is required.'
		
		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				'INSERT INTO img (title, author_id, hash, body)'
				' VALUES (?, ?, ?, ?)',
				(title, 'PLACEHOLDER', md5_hash, songs)
			)
			db.commit()
			return redirect(url_for('process.index'))
	return render_template('process/upload.html')


