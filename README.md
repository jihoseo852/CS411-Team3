# Snaptracks - Image-Based Music Recommendations

## CS411 - Team 3

## Written By
Jason Hong, Justin Taylor, Joseph Bain, Hunter Chun, Jiho Seo 

## Summary
Our project allows users to upload a photo (landscape, person, selfie, etc), and gives music recommendations based off of that photo. It aims to provide a fast, simple interface to quickly get a few song ideas that would fit the mood. In terms of the high-level features, we have implemented a SQLite database, 3rd party Google OAuth, and the Google Vision and Spotify API's. Our project also takes advantage of image caching, and by saving the MD5 Hash of the image files to the database, we prevent duplicate requests from slowing down the system.

### Usage

1. Get a Spotify and Google Credentials. You can get one [here](https://developer.spotify.com/dashboard/)

2. Set environment variables 

`export SPOT_ID="YOUR_SPOTIFY_DEV_CLIENT_ID"`

`export SPOT_SEC="YOUR_SPOTIFY_DEV_CLIENT_SECRET"`

`export GOOGLE_CLIENT_ID="YOUR_GOOGLE_CLIENT_ID"`

`export GOOGLE_CLIENT_SECRET="YOUR_GOOGLE_CLIENT_SECRET"`

`export GOOGLE_APPLICATION_CREDENTIALS="PATH_TO_CREDENTIALS_FILE.json"`

or alternatively add them in your .bashrc

3. Set Flask Application env

`export FLASK_APP='snaptracks'`

`export FLASK_ENV='development'`

4. `cd` into the root directory, and run `python -m flask init-db`. This will initialize a local sqlite database.

5. Run `python -m flask run`. Navigate to your browser and visit `http://127.0.0.1:5000/` to use Snaptracks

## Emails
Hunter Chun - hunterch@bu.edu

Justin Taylor - jdtaylor@bu.edu

Jiho Seo - jihoseo@bu.edu

Jason Hong - jason810@bu.edu

Joseph Bain - jbain359@bu.edu 


