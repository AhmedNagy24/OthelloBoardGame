def evaluation(board):
    black_score = board.count("b")
    white_score = board.count("w")
    return white_score - black_score


def game_over(board):
    empty = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "":
                empty += 1
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


def generate_children(board, turn):
    valid_moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == "" and check_adjacent(board, i, j, turn):
                valid_moves.append((i, j))
    return valid_moves


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluation(board), -1, -1

    if maximizing_player:
        max_eval = float("-inf")
        max_row = -1
        max_col = -1
        for (row, col) in generate_children(board, "w"):
            new_board = board.copy()
            new_board[row][col] = "w"
            value, _, _ = minimax(new_board, depth - 1, alpha, beta, False)
            if max_eval < value:
                max_eval = value
                max_row = row
                max_col = col
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return max_eval, max_row, max_col

    else:
        min_eval = float("inf")
        min_row = -1
        min_col = -1
        for (row, col) in generate_children(board, "b"):
            new_board = board.copy()
            new_board[row][col] = "b"
            value, _, _ = minimax(new_board, depth - 1, alpha, beta, True)
            if min_eval > value:
                min_eval = value
                min_row = row
                min_col = col
            beta = min(beta, value)
            if beta <= alpha:
                break
        return min_eval, min_row, min_col
#
# # initial call
# minimax(current_position, 3, float("-inf"), float("inf"), True)
