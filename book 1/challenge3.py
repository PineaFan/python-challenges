days = input("Choose an amount of days >")
try:
	days = float(days)
except ValueError:
	print("Not a valid number")
	exit()
assert days > 0, "Must be above 0"

print(f"{days} days is {days*24} hours, {days*24*60} minutes and {days*24*60*60} seconds")
