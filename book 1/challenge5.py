messages = {
	1: "Thank you",
	2: "Well done",
	3: "Correct"
}

try:
	print(messages[int(input("Enter 1 2 or 3 >"))])
except KeyError:
	print("Error message")
