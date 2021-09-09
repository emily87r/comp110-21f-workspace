"""Counting letters in a string."""

__author__ = "730240336"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
index = len(word) - 1
stop = word[index]
counter: int = 0

while index >= 0:
    if stop == letter:
        counter = counter + 1
        index = index - 1 
        stop = word[index]
    else:
        index = index - 1
        stop = word[index]
print("Count: " + str(counter))