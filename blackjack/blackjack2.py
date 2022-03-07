#!/usr/bin/env python3

import random

def dealer():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    cardSuit1 = random.choice(suits)
    cardValue1 = random.choice(value)

    cardSuit2 = random.choice(suits)
    cardValue2 = random.choice(value)

    print(f"You were dealt {cardValue1} of {cardSuit1}.")
    print(f"You were dealt {cardValue2} of {cardSuit2}.")
dealer()
