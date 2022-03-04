#!/usr/bin/env python3

def vendors():
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
    
    approved_vendors = ["cisco", "juniper", "big_ip"]
    
    for x in vendors:
        print(f"\nThe vendor is {x}", end="")
        if x not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")
vendors()

def farms():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    for y in farms:
        print(y.get("name", "Animal Farm"), end=":\n")
        for agri in y.get("agriculture"):
            print("  -", agri)
farms()
