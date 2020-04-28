import os
import base64
import json
import requests
import sys
import io
from . import vision
from . import spotify

def process(path):
	#fetches keywords from visionimg.py
	keywords = vision.visionapi(path)

	#fetches songs from spotifytracksearch.py
	print('')
	print('Songs:')
	result = []
	for x in range(len(keywords)):
		result.append(spotify.spotifysearch(keywords[x],'1'))

	#prints array containing songs, this array can be used to play the songs
	print('')
	print('Result Array:')
	print(result)

	return result
