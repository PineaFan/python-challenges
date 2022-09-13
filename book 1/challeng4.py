kg = input("Choose an amount in kg >")
try:
	kg = float(kg)
except ValueError:
	print("Not a valid number")
	exit()
assert kg > 0, "Must be above 0"

print(f"There are {2.204*kg} pounds in {kg} kg")
