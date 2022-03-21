# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age1 = int(age)

months = (90*12) - (age1*12)
weeks = (90*52) - (age1*52)
days = (90*365) - (age1*365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
