print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
bill_and_tip = bill + bill * tip_percentage
total_per_person =  round(bill_and_tip / people, 2)

print(f"${total_per_person}")


