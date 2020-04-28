# CS411 - Team 3 - Snaptracks

## Authors
Hunter Chun - hunterch@bu.edu

Justin Taylor - jdtaylor@bu.edu

Jiho Seo - jihoseo@bu.edu

Jason Hong - jason810@bu.edu

Joseph Bain - jbain359@bu.edu 

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




