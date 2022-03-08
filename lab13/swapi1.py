#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Star Wars API HTTP response parsing"""

from pprint import pprint
import json
import requests

# URL = "https://swapi.dev/luke/force"
URL= "https://swapi.dev/api/people/4/"

def main():
    """sending GET request, checking response"""

    resp= requests.get(URL)

    if resp.status_code == 200:
        vader= resp.json()
        pprint(vader)
        print(vader["name"])

    else:
        print("That is not a valid URL.")

if __name__ == "__main__":
    main()
