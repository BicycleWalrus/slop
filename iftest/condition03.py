#!/usr/bin/env python3
"""TPatrick | Alta3
   Fun with conditionals!"""

# Allowing the user to input the Hostname
hostname = input("What value should we set for hostname? ")

# If statement to check if the hostname matches - MTG when lowered
if hostname.lower() == "mtg":
    print("The hostname was foung to be mtg")
    print("Hostname matches expected configuration.")

# Saying goodbye
print("Exiting the script")
