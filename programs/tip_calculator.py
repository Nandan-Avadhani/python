#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#print("welcome to the tip calculator!")
bill =float(input("what is the total bill?\n"))
tip =int(input("how much percentage of tip would you like to give 10, 12, or 15?\n"))
people =int(input("how many people to split the bill?\n"))
tip_percentage = (tip/100)*bill 
bill_amount = bill + tip_percentage
final_bill = bill_amount/people
final_amount = round(final_bill,2)
print(f"each person has to pay:${final_amount}")























