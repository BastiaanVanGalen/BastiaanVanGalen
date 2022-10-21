age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆
lifespanLeft = 90 - int(age)
lifespanLeftInWeeks = lifespanLeft * 52
lifespanLeftInMonths = lifespanLeft * 12
lifespanLeftInDays = lifespanLeft * 365
print(f"You have {lifespanLeftInDays} days, {lifespanLeftInWeeks} weeks {lifespanLeftInMonths} months")
