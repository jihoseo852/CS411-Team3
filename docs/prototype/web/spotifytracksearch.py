import requests

url = "https://api.spotify.com/v1/search?q=sunset&type=track"

payload  = {}
headers = {
  'Authorization': 'Bearer BQCuM1wT6GURVYYHo7gnuW6H5uZnxG0LnlxB8fkhnkEniCP7_cXA6mdzn58c8QpQxP-flC9wtE68RH7WXKU3dCrRHzLIoQPrqHl256JB74hFPHLoaWrqSb9my02ndPAmufEz5ADF4f6Qjac0',
  'Cookie': '_ga=GA1.2.1005539955.1585257596; _gid=GA1.2.1275238351.1585257596'
}

response = requests.request("GET", url, headers=headers, data = payload)

data = response.json()

for x in range (1,10):
    print(data["tracks"]["items"][x]["name"])

