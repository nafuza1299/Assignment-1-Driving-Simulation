def cupsnball():
    cups = str(input()).upper()
    ball_position = 1
    for i in range(1, len(cups)):
        if "A" in cups:
            if ball_position == 1: #Starting position
                ball_position += 1
            elif ball_position == 2:#If the next command is "A" again, this will rotate the ball back to it's original position
                ball_position -= 1

        if "B" in cups:
            if ball_position == 2:
                ball_position += 1
            elif ball_position == 3:#Each letter has two possible positions
                ball_position -= 1

        if "C" in cups:
            if ball_position == 3:
                ball_position -= 2
        elif ball_position == 1:
                ball_position += 2
    print(ball_position)
    return
cupsnball()
