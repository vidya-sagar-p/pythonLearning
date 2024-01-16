print("welcome to the bill generator")
bill = float(input("What is the total bill ?"))
tip = float(input("what percentage bill would you like to give ? 10, 12 or 15? "))
people = int(input("how many people to split the bill ?"))
split_amount = ((bill * (tip/100)) + bill)/people
print(f"Each person should pay : ${round(split_amount,2)}")
# we can also use {:.2f}.format(split_amount) instead of round*
