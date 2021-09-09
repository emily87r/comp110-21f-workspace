"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730240336"

from random import randint

print("Your fortune cookie says...")
fortune: int = randint(1, 100)

if fortune == 50:
    print("You'll find love soon!")
else:
    if fortune > 50:
        print("Good things are coming!")
    else:
        if fortune > 25: 
            print("Look out for a shooting star.")
        else: 
            print("Something crazy is going to happen.")

print("Now, go spread positive vibes!")