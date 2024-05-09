import Board
from tkinter import messagebox
import AlphaBeta


class GameController:
    def __init__(self, player1_name, player2_name, difficulty):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 2
        self.player2_score = 2
        self.turn = "b"
        self.difficulty = difficulty

    def update_board(self, buttons, row, col):
        old_turn = Board.update_board(buttons, row, col, self.turn)
        if old_turn is None:
            return
        if self.turn == "b":
            if self.player2_name == "Computer":
                Board.outflank(buttons, row, col, old_turn)
                board_copy = Board.generate_2d_array(buttons)
                print(self.difficulty)
                _, computer_row, computer_col = AlphaBeta.minimax(board_copy, self.difficulty, float("-inf"), float("inf"), True)
                if computer_row == -1 and computer_col == -1:
                    return "w"
                print(computer_row, computer_col)
                Board.update_board(buttons, computer_row, computer_col, "w")
                Board.outflank(buttons, computer_row, computer_col, "w")
                return "w"
            else:
                self.turn = "w"
        else:
            self.turn = "b"
        return old_turn

    def check_adjacent(self, buttons, row, col, turn):
        rev_turn = "w" if self.turn == "b" else "b"
        for i in range(row-1, 0, -1):
            if buttons[i][col]["text"] == turn and i+1 != row:
                return True
            elif buttons[i][col]["text"] != rev_turn:
                break

        for i in range(row+1, 8):
            if buttons[i][col]["text"] == turn and i-1 != row:
                return True
            elif buttons[i][col]["text"] != rev_turn:
                break

        for i in range(col-1, 0, -1):
            if buttons[row][i]["text"] == turn and i+1 != col:
                return True
            elif buttons[row][i]["text"] != rev_turn:
                break

        for i in range(col+1, 8):
            if buttons[row][i]["text"] == turn and i-1 != col:
                return True
            elif buttons[row][i]["text"] != rev_turn:
                break
        return False

    def generate_valid_move(self, buttons, turn):
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if buttons[i][j]["text"] == "" and self.check_adjacent(buttons, i, j, turn):
                    valid_moves.append((i, j))
        if len(valid_moves) == 0 and self.player2_name != "Computer":
            if turn == "b":
                turn = "w"
            else:
                turn = "b"
            for i in range(8):
                for j in range(8):
                    if buttons[i][j]["text"] == "" and self.check_adjacent(buttons, i, j, turn):
                        valid_moves.append((i, j))
        elif len(valid_moves) == 0 and self.player2_name == "Computer" and turn == "b":
            board_copy = Board.generate_2d_array(buttons)
            print(self.difficulty)
            _, computer_row, computer_col = AlphaBeta.minimax(board_copy, self.difficulty, float("-inf"), float("inf"), True)
            if computer_row == -1 and computer_col == -1:
                return []
            print(computer_row, computer_col)
            Board.update_board(buttons, computer_row, computer_col, "w")
            Board.outflank(buttons, computer_row, computer_col, "w")
        self.turn = turn
        return valid_moves

    def end_game(self):
        if self.player1_score > self.player2_score:
            messagebox.showinfo("Game Over", self.player1_name + " won the game")
        elif self.player1_score < self.player2_score:
            messagebox.showinfo("Game Over", self.player2_name + " won the game")
        else:
            messagebox.showinfo("Game Over", "Game is a draw")

    def count_score(self, buttons):
        self.player1_score = 0
        self.player2_score = 0
        for i in range(8):
            for j in range(8):
                if buttons[i][j]["text"] == "b":
                    self.player1_score += 1
                elif buttons[i][j]["text"] == "w":
                    self.player2_score += 1
        return self.player1_score, self.player2_score
