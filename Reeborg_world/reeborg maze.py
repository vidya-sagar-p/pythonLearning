def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_right()
    while front_is_clear() and right_is_clear():
        move()
        if right_is_clear():
            turn_right()
            move()


# for i in range(6):
while at_goal() != True:
    if wall_in_front() and right_is_clear():
        jump()
    elif wall_in_front() and wall_on_right():
        turn_left()
        while front_is_clear():
            move()
    #   elif right_is_clear():
    #       turn_right()
    else:
        move()