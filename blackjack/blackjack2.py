#!/usr/bin/env python3
"""Tpatrick | Alta3
   Making a random 2 Card dealer"""

import random

def dealer():
    """Our Dealer Application"""
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    card_suit1 = random.choice(suits)
    card_value1 = random.choice(value)

    card_suit2 = random.choice(suits)
    card_value2 = random.choice(value)

    print(f"You were dealt {card_value1} of {card_suit1}.")
    print(f"You were dealt {card_value2} of {card_suit2}.")
dealer()
