import os
import base64
import json
import requests
import sys
import io
import visionimg
import spotifytracksearch

path = sys.argv[1]

#fetches keywords from visionimg.py
keywords = visionimg.visionapi(path)

#fetches songs from spotifytracksearch.py
print('')
print('Songs:')
result = []
for x in range(len(keywords)):
	result.append(spotifytracksearch.spotifysearch(keywords[x],'1'))

#prints array containing songs, this array can be used to play the songs
print('')
print('Result Array:')
print(result)
