print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is their name?\n") # What is their name?
print("The Love Calculator is calculating your score...")
couple=name1+name2
print(couple)
t=0
r=0
u=0
e=0
t += couple.lower().count("t")
r += couple.lower().count("r")
u += couple.lower().count("u")
e += couple.lower().count("e")
true_tot = str(t+r+u+e)
print(true_tot)
l=0
o=0
v=0
e=0
l += couple.lower().count("l")
o += couple.lower().count("o")
v += couple.lower().count("v")
e += couple.lower().count("e")
love_tot = str(l+o+v+e)
print(love_tot)
love_score = int(true_tot+love_tot)
print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
