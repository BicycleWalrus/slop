#!/usr/bin/env python3

print("Answer me these three questions please. ")
userquest = input("What is your quest? ")
usercolor = input("What is your favorite color? ")
userswallow = input("What is the air speed velocity of an unladen swallow? ")

print("Ah, I see. You're on a quest to " + userquest + " and your favorite color is " + usercolor + ". Sadly, your answer to my final question: " + userswallow + " was woefully dissapointing.")
print()

answers = {"Quest": userquest, "color": usercolor, "swallow": userswallow}

print("Your answers have been recorded and shall be used against you.")
print( answers )
