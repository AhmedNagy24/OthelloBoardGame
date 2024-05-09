from PIL import Image, ImageTk


def update_board(buttons, row, col, turn):
    image = None
    if turn == "w":
        image = Image.open("white.png")
    elif turn == "b":
        image = Image.open("black.png")
    if image is not None:
        image = image.resize((55, 55))
        photo = ImageTk.PhotoImage(image)
        if turn == "w":
            buttons[row][col].config(image=photo, width=46, height=50, text="w")
        else:
            buttons[row][col].config(image=photo, width=46, height=50, text="b")
        buttons[row][col].image = photo
        return turn
    return None


def outflank(buttons, row, col, turn):
    for i in range(row - 1, 0, -1):
        if buttons[i][col]["text"] == turn and i + 1 != row:
            for itr_row in range(row, i, -1):
                update_board(buttons, itr_row, col, turn)
            break
        elif buttons[i][col]["text"] == "":
            break

    for i in range(row + 1, 8):
        if buttons[i][col]["text"] == turn and i - 1 != row:
            for itr_row in range(row, i):
                update_board(buttons, itr_row, col, turn)
            break
        elif buttons[i][col]["text"] == "":
            break

    for i in range(col - 1, 0, -1):
        if buttons[row][i]["text"] == turn and i + 1 != col:
            for itr_col in range(col, i, -1):
                update_board(buttons, row, itr_col, turn)
            break
        elif buttons[row][i]["text"] == "":
            break

    for i in range(col + 1, 8):
        if buttons[row][i]["text"] == turn and i - 1 != col:
            for itr_col in range(col, i):
                update_board(buttons, row, itr_col, turn)
            break
        elif buttons[row][i]["text"] == "":
            break


def generate_2d_array(buttons):
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(buttons[i][j]["text"])
        board.append(row)
    return board
