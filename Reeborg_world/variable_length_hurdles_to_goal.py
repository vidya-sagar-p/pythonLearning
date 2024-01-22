def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# for i in range(6):
while at_goal() != True:
    if front_is_clear() is True:
        move()
    elif wall_in_front() is True:
        jump()












