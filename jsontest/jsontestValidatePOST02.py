#!/usr/bin/env python3
"""TPatrick | Alta3 Research
   Validating JSON POST Requests"""

import requests

timeurl = "http://date.jsontest.com"
ipurl = "http://ip.jsontest.com"
validurl = "http://validate.jsontest.com/"

def main():
    resp = requests.get(timeurl)
    mytime = resp.json()
    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    resp = requests.get(ipurl)
    myip = resp.json()
    print(myip)

    myip = myip["ip"]

    with open("/home/student/slop/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    jsontotest = {}
    jsontotest["time"] = mytime
    jsontotest["ip"] = myip
    jsontotest["mysvrs"] = mysvrs

    mydata = {}
    mydata["json"] = str(jsontotest)

    resp = requests.post(validurl, data=mydata)

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
