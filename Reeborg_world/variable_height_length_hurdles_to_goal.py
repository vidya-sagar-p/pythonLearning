#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb():
    turn_left()
    while wall_on_right() is True:
        move()


def fall():
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() is True and at_goal() != True:
        if front_is_clear() is True:
            move()
        else:
            turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# for i in range(6):
while at_goal() != True:
    if wall_in_front() is True and wall_on_right() is True:
        climb()
    elif right_is_clear() is True:
        fall()
    else:
        move()

# while at_goal() != True:
#     if wall_in_front():
#         jump()
#     else:
#         move()
