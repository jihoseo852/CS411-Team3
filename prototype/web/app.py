import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
	return render_template('fileform.html')

if __name__ == '__main__':
	app.run()
