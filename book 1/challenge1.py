price = input("How much was the total bill? > ")
price = price[1:] if price.startswith("£") else price
try:
	price = float(price)
except ValueError:
	print("Invalid amount")
	exit()

people = input("How many people are there? > ")
try:
	people = int(people)
except ValueError:
	print("Invalid amount")
	exit()

print(f"Each person needs to pay £{round(price/people, 2)}")
