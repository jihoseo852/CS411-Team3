import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
	if current_user.is_authenticated:
		return (render_template('index.html'))
	else:
		return '<a class="button" href="/login">Google Login</a>'

@app.route("/handleUpload", methods=['POST'])
def fileUpload():
	if 'photo' in request.files:
		photo = request.files['photo']
		if photo.filename != '':
			photo.save(os.path.join('/home/jason/Documents/JH/projects/411/prototype/files', photo.filename))
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()
