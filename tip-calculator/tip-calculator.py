print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
result = float(total_bill) * (float(percentage_tip) / 100)
print(f"{result}")
amount_people = input("How many people to split the bill? ")
result = result / int(amount_people)

print(f"Each person should pay: ${result}")