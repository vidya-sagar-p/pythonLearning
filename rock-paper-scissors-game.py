import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice < 3 and user_choice >= 0:
    print(image[user_choice])
    computer_choice = random.randint(0, 2)
    print("computer chose")
    print(image[computer_choice])

    '''
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)
 
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    '''
    if user_choice == 0:
        if computer_choice == 0:
            print("Draw")
        elif computer_choice == 1:
            print("You lose")
        else:
            print("You win")

    elif user_choice == 1:
        if computer_choice == 1:
            print("draw")
        elif computer_choice == 2:
            print("You lose")
        else:
            print("You win")

    elif user_choice == 2:
        if computer_choice == 2:
            print("Draw")
        elif computer_choice == 1:
            print("You lose")
        else:
            print("You win")


else:
    print("please choose only? Type 0 for Rock, 1 for Paper or 2 for Scissors.")