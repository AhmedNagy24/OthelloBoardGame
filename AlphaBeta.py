import State


def utility_function(board):
    white_score = 0
    black_score = 0

    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'w':
                white_score += 1
                min_distance = min(abs(i - corner[0]) + abs(j - corner[1]) for corner in corners)
                white_score += 1 / (min_distance + 1)
            elif board[i][j] == 'b':
                black_score += 1
                min_distance = min(abs(i - corner[0]) + abs(j - corner[1]) for corner in corners)
                black_score += 1 / (min_distance + 1)

    white_mobility = len(State.children_states(board, 'w'))
    black_mobility = len(State.children_states(board, 'b'))

    white_score += white_mobility
    black_score += black_mobility

    return white_score - black_score


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or State.game_over(board):
        return utility_function(board), -1, -1

    if maximizing_player:
        max_eval = float("-inf")
        max_row = -1
        max_col = -1
        children = State.children_states(board, "w")
        for (row, col) in children:
            new_board = board.copy()
            new_board[row][col] = "w"
            next_state = State.outflank(new_board, row, col, "w")
            value, _, _ = minimax(next_state, depth - 1, alpha, beta, False)
            if max_eval <= value:
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
        children = State.children_states(board, "b")
        for (row, col) in children:
            new_board = board.copy()
            new_board[row][col] = "b"
            next_state = State.outflank(new_board, row, col, "w")
            value, _, _ = minimax(next_state, depth - 1, alpha, beta, True)
            if min_eval >= value:
                min_eval = value
                min_row = row
                min_col = col
            beta = min(beta, value)
            if beta <= alpha:
                break
        return min_eval, min_row, min_col
