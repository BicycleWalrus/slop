#!/usr/bin/env python3
"""TPatrick | Alta3
   Using an HTTP GET to determine when the ISS will pass over head."""

import requests
import time

def latinput():
    while True:
        try:
            lat = float(input("What is your Latitude?\n"))
        except ValueError:
            print("Not a valid Latitude! Try again.")
            continue
        else:
            return lat
            break

def loninput():
    while True:
        try:
            lon = float(input("What is your Longitude?\n"))
        except ValueError:
            print("Not a valid Longitude! Try again.")
            continue
        else:
            return lon
            break

openurl = "http://api.open-notify.org/iss-pass.json?"
openurl += f"lat={latinput()}&lon={loninput()}"

def sam():
    """Named Sam because Sam doesn't like Main"""
    items = requests.get(f"{openurl}")
    items = items.json()

    for item in items.get("response"):
        print(f"{item['duration']}, at {time.ctime(item['risetime'])}")

if __name__ == "__main__":
    sam()
