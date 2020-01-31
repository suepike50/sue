import urllib.request
import json
import sys


def issnow():
    req = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    html = req.read()

    j = json.loads(html.decode("utf-8"))
    for x in j:
        print(x,j[x])


def isspass():
    req = urllib.request.urlopen("http://api.open-notify.org/iss-pass.json?lat=42.9907445&lon=-87.8809208,17")
    html = req.read()

    j = json.loads(html.decode("utf-8"))
    for x in j:
        print(x, j[x])

def issastros():
    req = urllib.request.urlopen("http://api.open-notify.org/astros.json")
    html = req.read()

    j = json.loads(html.decode("utf-8"))
    for x in j:
        print(x, j[x])

if __name__ == "__main__":
    try:
        option = sys.argv[1]
    except:
        option = "one"
    if option == "one":
        issnow()
    elif option == "two":
        isspass()
    elif option == "three":
        issastros()
    