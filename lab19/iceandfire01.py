#!/usr/bin/env python3
"""TPatrick | Alta3 Research
   Exploring OpenAPIs with requests"""

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    gotresp = requests.get(AOIF)

    got_dj = gotresp.json()

    print(got_dj)

if __name__ == "__main__":
    main()
