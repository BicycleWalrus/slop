#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   Reviewing how to parse json"""

import json

def main():
    """runtime code"""
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()
