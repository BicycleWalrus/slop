#!/usr/bin/env python3
"""TPatrick | Alta3 Research
   Astros Challenge"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import requests
from flask import render_template

MAJORTOM = "http://api.open-notify.org/astros.json"

def rise():
    grountctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()

    print("\n\nConverted Python Data")
    print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    return helmetson

app = Flask(__name__)
@app.route("/")
def hello_user():
    return people

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
