import random

names_string = input()
names = names_string.split(", ")
banker = random.randint(0, len(names)-1)
print(f"{names[banker]} is going to buy the meal today!")

