# 1st input: enter height in meters e.g: 1.65
height = float(input("enter you weight in meters: "))
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input("enter your weight in kgs: "))
BMI = (weight / (height ** 2))
if BMI <= 18.5:
    print(f"Your BMI is {round(BMI, 2)}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {round(BMI, 2)}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {round(BMI, 2)}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {round(BMI, 2)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI, 2)}, you are clinically obese.")


