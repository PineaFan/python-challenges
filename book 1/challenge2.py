import math

number = input("Choose a number over 100 > ")
try:
	number = int(number)
except ValueError:
	print("Not a valid number")
	exit()
assert number > 100, "Must be above 100"

denominator = input("Choose a number to divide by > ")
try:
	denominator = int(denominator)
except ValueError:
	print("Not a valid number")
	exit()
assert denominator < 10, "Must be below 10"

print(f"{denominator} can go into {number} {math.floor(number/denominator)} times")
