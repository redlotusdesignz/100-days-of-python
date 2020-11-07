#Ask for inputs of the bill, percentage, people

print("Tip Calculator\n")
bill = input("What's the total bill? ")
percentage = input("What percentage tip you would like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#Convert the inputs to inte
bill_num = float(bill)
percentage_num = int(percentage)
people_num = int(people)

tip = bill_num+(bill_num * (percentage_num / 100))
final_bill = round(tip/people_num,2)

print(f"Each person should pay: ${final_bill}")
