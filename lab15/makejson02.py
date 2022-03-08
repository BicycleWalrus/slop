#!/usr/bin/env python3

"""TPatrick | Alta3 Research
   json.dumps() function creates a JSON string"""

import json

def main():
    """runtime code"""
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)

if __name__ == "__main__":
    main()
