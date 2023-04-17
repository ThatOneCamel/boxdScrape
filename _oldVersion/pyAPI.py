import urllib.request
import re
from requests_html import HTMLSession

#url = "https://letterboxd.com/tommypedersen/list/2016/"
url = "https://letterboxd.com/tommypedersen/list/tommys-movie-collection/page/3/"

session = HTMLSession()
resp = session.get(url)
 
#resp.html.render(scrolldown=10, timeout=30)
titles = resp.html.find('.numbered-list-item')
for title in titles:
	print(title.text)

f = open("htmlcontent.txt", "w")
f.write(resp.html.html)
f.close()

def getPage(url):
	try:
		response = urllib.request.urlopen(url)
		print("Established connection")
		data = response.read()
		page = data.decode("utf8")


		#Pure html solution.
		x = list(re.findall("alt=\"(.*?)\"", page))
		x.pop(0)
		i = 1
		for item in x:
			print("[{}] {}".format(i, item))
			i += 1
	
		response.close()
		return x
		
	except Exception as e:
		print(e)
		print("Failed to retrieve info from webpage")
		return set()

myStr = getPage(url)