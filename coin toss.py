import random

pick = input('what\'s your call ? "Heads" or "Tails"')
print("tossing the coin ...")
toss = random.randint(0,1)
if toss == 1:
    print("Heads")
else:
    print("Tails")
