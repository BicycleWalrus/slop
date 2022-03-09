#!/usr/bin/env python3

import requests
import json

GETURL = "http://validate.jsontest.com/"

def main():
    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    jsontovalidate = f"json={ json.dumps(mydata).replace(' ', '') }"
    resp = requests.get(f"{GETURL}?{jsontovalidate}")

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
