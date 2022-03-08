#!/usr/bin/env python3

"""TPatrick | Alta3
   Opening a static file containing JSON data"""

import json

def main():
    """runtime code"""
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    datacenterdecoded = json.loads(datacenterstring)

    print(type(datacenterdecoded))

    print(datacenterdecoded)

    print(datacenterdecoded["row3"])

    print(datacenterdecoded["row2"][1])

if __name__ == "__main__":
    main()
