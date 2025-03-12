#this is a tip and final per person bill calculator
print("Welcome to the tip calculator!")
#takes input from user
bill_amount = float(input('What was the total bill?\n'))
tip_percent = int(input("How much % tip would you like to give? 10, 12, or 15?\n"))
total_people = int(input("How many people to split the bill?\n"))
#calculates the total bill amount with tip included
final_bill = bill_amount+(bill_amount*(tip_percent/100))
#calculates the per-person amount
per_head = final_bill/total_people
#prints the final per-person amount upto 2 decimal places
print(f"Each person should pay: {round(per_head,2)}")
