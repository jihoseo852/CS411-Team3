# Prototype HTML, CSS, and JavaScript files

## Dependencies
This project requires the following dependencies

[Google Cloud Vision API](https://cloud.google.com/vision/docs/setup)

[Spotify Developer API](https://developer.spotify.com/dashboard/)

`pip install flask`

## Usage

Replace Filesystem Pointers

Currently, the system is set to `/home/jason/.../photodb`. Locate the pointer in process.py and change this directory to point to your project location. 

Initialize the db:

`set FLASK_APP=snaptrack`

`set FLASK_ENV=development`

`python -m flask init-db`

Run

On Python v.3+ run `python -m flask run` on the root directory. Then navigate to your browser and go to `http://127.0.0.1:5000/`. 


