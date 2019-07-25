n, m = map(int, input().split())
board = []
b_location = None
r_location = None
for i in range(n):
    tmp = list(input())
    for j, char in enumerate(tmp):
        if char == "B":
            b_location = (i, j)
        elif char == "R":
            r_location = (i, j)
        elif char == "O":
            o_location = (i, j)
    board.append(tmp)


def move_left(main_ball, compare_ball):
    if main_ball == (-100, -100):
        return main_ball
    while True:
        main_x, main_y = main_ball
        if board[main_x][main_y - 1] != "#":
            if (main_x, main_y - 1) != compare_ball:
                main_y -= 1
                if (main_x, main_y) == o_location:
                    main_x = -100
                    main_y = -100
                    return main_x, main_y
        if (main_x, main_y) == main_ball:
            return main_x, main_y
        else:
            main_ball = main_x, main_y


def move_right(main_ball, compare_ball):
    if main_ball == (-100, -100):
        return main_ball
    while True:
        main_x, main_y = main_ball
        if board[main_x][main_y + 1] != "#":
            if (main_x, main_y + 1) != compare_ball:
                main_y += 1
                if (main_x, main_y) == o_location:
                    main_x = -100
                    main_y = -100
                    return main_x, main_y
        if (main_x, main_y) == main_ball:
            return main_x, main_y
        else:
            main_ball = main_x, main_y


def move_up(main_ball, compare_ball):
    if main_ball == (-100, -100):
        return main_ball
    while True:
        main_x, main_y = main_ball
        if board[main_x - 1][main_y] != "#":
            if (main_x - 1, main_y) != compare_ball:
                main_x -= 1
                if (main_x, main_y) == o_location:
                    main_x = -100
                    main_y = -100
                    return main_x, main_y
        if (main_x, main_y) == main_ball:
            return main_x, main_y
        else:
            main_ball = main_x, main_y


def move_down(main_ball, compare_ball):
    if main_ball == (-100, -100):
        return main_ball
    while True:
        main_x, main_y = main_ball
        if board[main_x + 1][main_y] != "#":
            if (main_x + 1, main_y) != compare_ball:
                main_x += 1
                if (main_x, main_y) == o_location:
                    main_x = -100
                    main_y = -100
                    return main_x, main_y
        if (main_x, main_y) == main_ball:
            return main_x, main_y
        else:
            main_ball = main_x, main_y


def going(red_ball, blue_ball, method):
    while True:
        red_x, red_y = method(red_ball, blue_ball)
        blue_x, blue_y = method(blue_ball, red_ball)
        if (red_x, red_y) == red_ball and (blue_x, blue_y) == blue_ball:
            break
        else:
            red_ball = red_x, red_y
            blue_ball = blue_x, blue_y
    return red_ball, blue_ball


def move(red_ball, blue_ball, method):
    if method == "left":
        return going(red_ball, blue_ball, move_left)
    elif method == "right":
        return going(red_ball, blue_ball, move_right)
    elif method == "up":
        return going(red_ball, blue_ball, move_up)
    else:
        return going(red_ball, blue_ball, move_down)


# print(move(r_location, b_location, "left"))
# print(move(r_location, b_location, "right"))
# print(move(r_location, b_location, "up"))
# print(move(r_location, b_location, "down"))

pair_movements1 = ["left", "right"]
pair_movements2 = ["up", "down"]
queue = [(r_location, b_location, "left", 1),
         (r_location, b_location, "right", 1),
         (r_location, b_location, "up", 1),
         (r_location, b_location, "down", 1),
         ]
last = queue[-1]
answer = -1
while queue:
    # print(queue, "queue")
    current = queue.pop(0)
    # print(current, "current")
    r_cur, b_cur, method, tmp = current
    if tmp > 10:
        answer = -1
        break
    r_move, b_move = move(r_cur, b_cur, method)
    # print(r_cur, r_move, b_cur, b_move, "check point")
    if b_move == (-100, - 100): continue
    if (r_cur, b_cur) == (r_move, b_move): continue
    if r_move == (-100, -100):
        answer = tmp
        break
    if method in pair_movements1:
        for movement in pair_movements2:
            queue.append((r_move, b_move, movement, tmp + 1))
    else:
        for movement in pair_movements1:
            queue.append((r_move, b_move, movement, tmp + 1))
    # for movement in pair_movements1 + pair_movements2:
    #     if movement != method:
    #         queue.append((r_move, b_move, movement, tmp + 1))

print(answer)
