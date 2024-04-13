#Calculate the tip you have to pay at a restaurant

print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $\n>")
total_bill = float(total_bill)

tip_amount = input("How much tip would you like to give? %\n>")
tip_amount = float(tip_amount)

split_bill = input("How many people to split the bill? \n>")
split_bill = float(split_bill)

total_to_pay_with_tips = total_bill + ((tip_amount/100) * total_bill)
total_to_pay_with_tips = float(total_to_pay_with_tips)

#calculate how much each person has to pay
each_person = total_to_pay_with_tips/split_bill
each_person = float(round(each_person, 2))

print(f"Each person should pay: ${each_person}")