#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator \n")

bill = input("What was the total bill\n")
tip = input("How much tip would you like to give?\n")
split = input("How many people to split the bill?\n ")

bill1 = float(bill)
tip1 = int(tip)
split1 = int(split)

tip_as_percent = float(tip1/100)
tip_bill_total = bill1*tip_as_percent
total_bill = bill1+tip_bill_total
bill_per_person = total_bill/split1
final_amount = round(bill_per_person,2)

print(f"Each person should pay: ${final_amount}")