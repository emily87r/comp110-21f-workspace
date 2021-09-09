"""Repeating a beat in a loop."""

__author__ = "730240336"


beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
counter = 1
repeat = beat

if number <= 0:
    print("No beat...")
else:
    while counter < number:
        repeat = repeat + " " + beat
        counter = counter + 1
    print(repeat)
