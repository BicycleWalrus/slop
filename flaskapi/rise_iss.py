#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Astros on ISS"""

import requests
from flask import Flask

app = Flask(__name__)
MAJORTOM = "http://api.open-notify.org/astros.json"

def rise():
    """reading json from api"""
    groundctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()
    
    print("\n\nConverted Python Data")
    print(helmetson)

@app.route("/")
@app.route("/<craft>")
def craft_crew(craft="ISS"):
    people = rise()["people"]
    crew = []
    for astro in people:
        if astro['craft'] == craft:
            crew.append(astro['name'])
    return "\n".join(crew)

if __name__ == "__main__":
    app.run(port=2224)
