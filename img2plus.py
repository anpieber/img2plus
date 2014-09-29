import httplib
import urlparse

from oauth2client.client import flow_from_clientsecrets

headers = {"Content-Type":"application/json"}
url = "https://picasaweb.google.com/data/feed/api/user/101458158860096958252"
domain = urlparse.urlparse(url).netloc
connection = httplib.HTTPSConnection(domain)
connection.request("GET", url, headers=headers)
response = connection.getresponse()

print "status: " + str(response.status), response.reason
print response.getheaders()
print response.read()
