from collections import deque


def move(command, position, size):  # calculate new position in field
    def command_validate(x_new, y_new, size):  # validate new position (are indices valid?)
        is_x_new_valid = 0 <= x_new < size
        is_y_new_valid = 0 <= y_new < size
        if is_x_new_valid and is_y_new_valid:
            return True
        else:
            return False

    x_position, y_position = position
    x_increment, y_increment = command
    x_new, y_new = x_position + x_increment, y_position + y_increment  # calculate new position
    if not command_validate(x_new, y_new, size):  # call validate function, return old position if not valid
        return x_position, y_position
    else:
        return x_new, y_new  # return new coordinates


def count_coals_and_start_position(field, size):  # count coals in field and return starting position
    coals_count = 0
    start = None
    for i in range(size):
        for j in range(size):
            if field[i][j] == "c":
                coals_count += 1
            elif field[i][j] == "s":
                start = (i, j)
    return coals_count, start


size = int(input())
commands_possible = {  # assign raw commands to row/col coordinate increments
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

commands = deque((commands_possible[command] for command in input().split()))  # put commands in a deque as tuples of coordinate increments
field = [[element for element in input().split()] for _ in range(size)]  # construct field from input
coals_count, position_starting = count_coals_and_start_position(field, size)  # fetch coals count and starting position

position_current = position_starting
coals_found = 0
while commands:  # evaluate field
    command_current = commands.popleft()  # fetch current command
    position_current = move(command_current, position_current, size)  # execute move command, get new position
    x_current, y_current = position_current  # current coordinates
    if field[x_current][y_current] == "e":  # break if found end
        print(f"Game over! ({x_current}, {y_current})")
        break
    elif field[x_current][y_current] == "c":  # found coal
        field[x_current][y_current] = "*"
        coals_found += 1
        if coals_found == coals_count:  # break if found all coal
            print(f"You collected all coals! ({x_current}, {y_current})")
            break



else:  # if not all coals found and not found end after all commands executed, print coals left and current coordinates
    coals_left = coals_count - coals_found
    x_current, y_current = position_current
    print(f"{coals_left} coals left. ({x_current}, {y_current})")
