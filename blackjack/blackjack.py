#!/usr/bin/env python3

import random

#Dictionary/Lists for the cards

cards = {}

def dealer():
    cards["Hearts"] = ['Ace', 'Two', 'Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    
    cards["Diamonds"] = ['Ace', 'Two', 'Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    
    cards["Spades"] = ['Ace', 'Two', 'Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    
    cards["Clubs"] = ['Ace', 'Two', 'Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    
    dealt = list(cards.items())
    
    Card1 = random.choice(dealt)
    Card2 = random.choice(dealt)
    
    print(f"You were dealt a {Card1} and {Card2}")
dealer()
