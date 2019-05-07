import urllib.request

request = urllib.request.Request('http://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode())