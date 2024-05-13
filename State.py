def game_over(board):
    empty = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "":
                empty += 1
    player_moves = children_states(board, "b")
    computer_moves = children_states(board, "w")
    if len(player_moves) == 0 and len(computer_moves) == 0:
        return True
    return empty == 0


def check_adjacent(board, row, col, turn):
    rev_turn = "w" if turn == "b" else "b"
    for i in range(row - 1, 0, -1):
        if board[i][col] == turn and i + 1 != row:
            return True
        elif board[i][col] != rev_turn:
            break

    for i in range(row + 1, 8):
        if board[i][col] == turn and i - 1 != row:
            return True
        elif board[i][col] != rev_turn:
            break

    for i in range(col - 1, 0, -1):
        if board[row][i] == turn and i + 1 != col:
            return True
        elif board[row][i] != rev_turn:
            break

    for i in range(col + 1, 8):
        if board[row][i] == turn and i - 1 != col:
            return True
        elif board[row][i] != rev_turn:
            break
    return False


def children_states(board, turn):
    states = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == "" and check_adjacent(board, i, j, turn):
                states.append((i, j))
    return states


def outflank(board, row, col, turn):
    output = board.copy()
    for i in range(row - 1, 0, -1):
        if output[i][col] == turn and i + 1 != row:
            for itr_row in range(row, i, -1):
                output[itr_row][col] = turn
            break
        elif output[i][col] == "":
            break

    for i in range(row + 1, 8):
        if output[i][col] == turn and i - 1 != row:
            for itr_row in range(row, i):
                output[itr_row][col] = turn
            break
        elif output[i][col] == "":
            break

    for i in range(col - 1, 0, -1):
        if output[row][i] == turn and i + 1 != col:
            for itr_col in range(col, i, -1):
                output[row][itr_col] = turn
            break
        elif output[row][i] == "":
            break

    for i in range(col + 1, 8):
        if output[row][i] == turn and i - 1 != col:
            for itr_col in range(col, i):
                output[row][itr_col] = turn
            break
        elif output[row][i] == "":
            break
    return output
