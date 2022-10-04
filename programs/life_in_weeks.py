# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_in_integer = int(age)
year_days = 365
year_weeks =52
year_months = 12
years_in_days_left =(90*365 - (age_in_integer *365))
years_in_weeks_left = (90*52 -(age_in_integer *52))
years_in_months_left = (90*12 - (age_in_integer *12))
print(f"You have {years_in_days_left} days, {years_in_weeks_left} weeks, and {years_in_months_left} months left.")



