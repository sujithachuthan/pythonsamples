from bs4 import BeautifulSoup
import urllib2

try:
    test_url = urllib2.urlopen("http://www.reddit.com")
    readHtml = test_url.read()
except urllib2.HTTPError, error:
    contents = error.read()

test_url.close()

soup = BeautifulSoup(readHtml)
# all_tag_a = soup.find_all("a", limit=10)
all_tag_a = soup.find_all("a")

print all_tag_a
for links in all_tag_a:
	print (links.get('href'))