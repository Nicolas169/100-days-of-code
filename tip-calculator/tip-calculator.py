print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_percentage_tip = float(total_bill) * (float(percentage_tip) / 100)

amount_people = input("How many people to split the bill? ")
total_bill = round((float(total_bill) + float(total_percentage_tip)) / int(amount_people), 2)

print(f"Each person should pay: ${total_bill}")
