chess_board = [input().split(" ") for i in range(8)]
mate = False
tl_indexx = 1
bl_indexx = 1
tr_indexx = 1
br_indexx = 1

for i in range(8):
    for j in range(8):
        if chess_board[i][j] == "K":
            current_row = i
            current_col = j

            # horizontal check - to the right
            for col in range(current_col + 1, 8):
                if chess_board[current_row][col] == "Q":
                    print([current_row, current_col])
                    break

            # horizontal check - to the left
            for col in range(current_col - 1, -1, -1):
                if chess_board[current_row][col] == "Q":
                    print([current_row, current_col])
                    break

            # vertical check - going down
            for row in range(current_row + 1, 8):
                if chess_board[row][current_col] == "Q":
                    print([current_row, current_col])
                    break

            # vertical check - going up
            for row in range(current_row - 1, -1, -1):
                if chess_board[row][current_col] == "Q":
                    print([current_row, current_col])
                    break

            # diagonal check - bottom-right
            for col in range(current_col + 1, 8):
                if current_row + br_indexx < 8:
                    if chess_board[current_row + br_indexx][col] == "Q":
                        print([current_row, current_col])
                        break
                    br_indexx += 1

            # diagonal check - top-right
            for col in range(current_col + 1, 8):
                if current_row - tr_indexx > -1:
                    if chess_board[current_row - tr_indexx][col] == "Q":
                        print([current_row, current_col])
                        break
                    tr_indexx += 1

            # diagonal check - bottom-left
            for col in range(current_col - 1, -1, -1):
                if current_row + bl_indexx < 8:
                    if chess_board[current_row + bl_indexx][col] == "Q":
                        print([current_row, current_col])
                        break
                    bl_indexx += 1

            # digonal check - top-left
            for col in range(current_col - 1, -1, -1):
                if current_row - tl_indexx > -1:
                    if chess_board[current_row - tl_indexx][col] == "Q":
                        print([current_row, current_col])
                        break
                    tl_indexx += 1

if not mate:
    print('The king is safe!')