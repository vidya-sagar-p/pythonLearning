
#'You're at a crossroad. Where do you want to go? Type "left" or "right"'
#'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
#"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
#"It's a room full of fire. Game Over."
#"You found the treasure! You Win!"
#"You enter a room of beasts. Game Over."
#"You chose a door that doesn't exist. Game Over."
#"You get attacked by an angry trout. Game Over."
#"You fell into a hole. Game Over."


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
stage1 = input('You\'re at a crossroad. Where do you want to go? Type "forest" or "broken bridge"\n')
level1_lower = stage1.lower()
if (level1_lower == "forest"):
    print("brave explorer! you have successfully crossed forest")
    level2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if (level2 == "wait"):
        print("You arrive at the island unharmed")
        level3 = input("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose\n?")
        level3_lower = level3.lower()
        if (level3_lower == "yellow"):
            print("congratulations adventurer. You found the treasure! You Win!")
        elif (level3_lower == "red"):
            print("You get burned in the wildfire. Game Over")
        elif (level3_lower == "blue"):
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("you were been attacked by crocodiles. game over")
else:
    print("you have been fallen bridge and your Game over")