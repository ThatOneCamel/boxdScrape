from flask import Flask
from flask import request
import urllib.request
import re
from requests_html import HTMLSession

app = Flask(__name__)

#Makes all responses plaintext
@app.after_request
def treat_as_plain_text(response):
    response.headers["content-type"] = "text/plain"
    return response

@app.route('/')
def getList():
    url = request.args.get("listurl")
    return getPage(url)

@app.route('/sample')
def getSampleList():
    return getPage("https://letterboxd.com/tommypedersen/list/tommys-movie-collection/page/3/")

#url = "https://letterboxd.com/tommypedersen/list/2016/"
url = "https://letterboxd.com/tommypedersen/list/tommys-movie-collection/page/3/"

session = HTMLSession()
resp = session.get(url)

def getPage(url):
    try:
        response = urllib.request.urlopen(url)
        print("Established connection")
        data = response.read()
        page = data.decode("utf8")


        #Pure html solution.
        films = list(re.findall("alt=\"(.*?)\"", page))
        films.pop(0)
        i = 1
        listStr = ""
        for movie in films:
            print("[{}] {}".format(i, movie))
            listStr += movie + "\n"
            i += 1
    
        response.close()
        return listStr
        
    except Exception as e:
        print(e)
        print("Failed to retrieve info from webpage")
        return set()

myStr = getPage(url)
