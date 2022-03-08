#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Astros on ISS"""

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    groundctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()
    
    print("\n\nConverted Python Data")
    print(helmetson)

    print("\n\nPeople in Space: ", helmetson['number'])
    people = helmetson['people']
    print(people)


if __name__ == "__main__":
    main()
