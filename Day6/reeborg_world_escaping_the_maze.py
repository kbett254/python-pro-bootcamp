def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        while front_is_clear():
            if not wall_in_front():
                move()
    else:
        turn_left()

