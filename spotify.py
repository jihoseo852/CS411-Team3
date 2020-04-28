import os
import base64
import json
import requests
import sys
def spotifysearch(keyword1,keyword2):
# Takes in environment variables and sets CLIENT_ID and CLIENT_SEC
	CLIENT_ID = os.getenv('SPOT_ID')
	CLIENT_SEC = os.getenv('SPOT_SEC')

# Spotify wants the CLIENT_ID:CLIENT_SEC to be base64 encoded, and formatted this way
	authStr = CLIENT_ID + ':' + CLIENT_SEC
	authID64 = base64.b64encode(authStr.encode('utf-8')).decode('utf-8')
	authID = 'Basic ' + authID64

# Token params
	tokenURL = "https://accounts.spotify.com/api/token"
	headers = {'Authorization': authID}
	payload = {'grant_type':'client_credentials'}

# HTTP request to post toekn
	resp = requests.post(tokenURL, headers = headers, data = payload)

	token = resp.json()
	token = 'Bearer ' + token['access_token']

#########

#Search paramaters, take in command line args for now
	searchTerm = "q=" + keyword1
	searchType = "type=track"
	searchMarket = "market=US"
	searchLimit = "limit=" + keyword2

	acceptedResp = "application/json"

# Query params
	payload = {}
	getURL = "https://api.spotify.com/v1/search?" + searchTerm + "&" + searchType + "&" + searchMarket + "&" + searchLimit
	headers = {
		'Authorization': token,
		'Accept': acceptedResp
	}

# Response
	searchResp = requests.get(getURL, headers = headers, data=payload)
	resp = searchResp.json()

	result = []
	for x in range(int(keyword2)):
		print(resp["tracks"]["items"][x]["name"])
		result.append(resp["tracks"]["items"][x]["name"])

	with open('data.txt','w') as outfile:
		json.dump(resp,outfile)

	return result

#url = "https://api.spotify.com/v1/search?q=sunset&type=track"

#payload  = {}
#headers = {
#  'Authorization': 'Bearer BQCuM1wT6GURVYYHo7gnuW6H5uZnxG0LnlxB8fkhnkEniCP7_cXA6mdzn58c8QpQxP-flC9wtE68RH7WXKU3dCrRHzLIoQPrqHl256JB74hFPHLoaWrqSb9my02ndPAmufEz5ADF4f6Qjac0',
#  'Cookie': '_ga=GA1.2.1005539955.1585257596; _gid=GA1.2.1275238351.1585257596'
#}

#response = requests.request("GET", url, headers=headers, data = payload)

#data = response.json()

#for x in range (1,10):
#    print(data["tracks"]["items"][x]["name"])

#with open('data.txt', 'w') as outfile:
#    json.dump(data,outfile)
