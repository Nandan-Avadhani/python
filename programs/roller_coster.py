# roller coster ride
# rules 
# 1 the rider must be 120 cm and taller
# 2 if the rider < 12 years pay 5 $
# 3 if the rider < 18 pay 7 $
# if the rider > 18 pay 12 $

print(" welcome to the heart bursting mind boggling roller coster ride")
height = int(input("enter your height in cm \n"))
if height >= 120:
    print("you are eligible for this ride")
    age = int(input(" enter your age\n"))
    if age < 12:
        print("pay 5 $")
    elif age < 18:
        print("pay 7 $")
    elif age > 18:
        print(" pay 12 $")
else:
    print(" you are not eligible for this ride")




