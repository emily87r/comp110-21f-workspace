"""A program to demonstrate how numeric operators can be used."""

_author_: str = "730240336"

left: str = input("Give me a random number, please!")
right: str = input("Give me another random number, please!")
left_int: int = int(left)
right_int: int = int(right)
print("Left-hand side: " + left)
print("Right-hand side: " + right)
print(str(left) + " ** " + str(right) + " is " + str(left_int ** right_int)) 
print(str(left) + " / " + str(right) + " is " + str(left_int / right_int))
print(str(left) + " // " + str(right) + " is " + str(left_int // right_int))
print(str(left) + " % " + str(right) + " is " + str(left_int % right_int))