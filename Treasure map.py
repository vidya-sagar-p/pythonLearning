line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().lower() # Where do you want to put the treasure?

if position[0] == "a":
    if int(position[1]) == 1:
        map[0][0] = 'X'
    elif int(position[1]) == 2:
        map[1][0] = 'x'
    elif int(position[1]) == 3:
        map[2][0] = 'X'
    else:
        print("insert ")

elif position[0] == "b":
    if int(position[1]) == 1:
        map[0][1] = 'X'
    elif int(position[1]) == 2:
        map[1][1] = 'x'
    elif int(position[1]) == 3:
        map[2][1] = 'X'
    else:
        print("insert a valid location")

elif position[0] == "c":
    if int(position[1]) == 1:
        map[0][2] = 'X'
    elif int(position[1]) == 2:
        map[1][2] = 'x'
    elif int(position[1]) == 3:
        map[2][2] = 'X'
    else:
        print("insert a valid location")

else:
    print("insert")




print(f"{line1}\n{line2}\n{line3}")