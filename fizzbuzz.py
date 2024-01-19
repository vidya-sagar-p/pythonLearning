target = 100
for number in range(1,target + 1):
  if number % 3 != 0 and number % 5 != 0:
    print(number)
  elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("Buzz")



