import Board
from tkinter import messagebox
import AlphaBeta
from Player import Player


class GameController:
    def __init__(self, player1_name, player2_name, is_comp, difficulty):
        self.player1 = Player(player1_name, 2, "b")
        self.player2 = Player(player2_name, 2, "w")
        self.turn = "b"
        if is_comp == 1:
            self.player2.isComputer = True
        self.difficulty = difficulty

    def update_board(self, buttons, row, col):
        old_turn = Board.update_board(buttons, row, col, self.turn)
        if old_turn is None:
            return
        if self.turn == "b":
            if not self.player2.isComputer:
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

    def get_moves(self, buttons):
        moves = []
        for i in range(8):
            for j in range(8):
                if buttons[i][j]["text"] == "" and self.check_adjacent(buttons, i, j, self.turn):
                    moves.append((i, j))
        return moves

    def generate_valid_move(self, buttons):
        valid_moves = self.get_moves(buttons)
        if len(valid_moves) == 0 and not self.player2.isComputer:
            if self.turn == "b":
                self.turn = "w"
            else:
                self.turn = "b"
            valid_moves = self.get_moves(buttons)
        elif len(valid_moves) == 0 and self.player2.isComputer and self.turn == "b":
            check = self.computer_turn(buttons)
            if not check:
                return []
            valid_moves.clear()
            valid_moves = self.get_moves(buttons)
        return valid_moves

    def end_game(self):
        if self.player1.score > self.player2.score:
            messagebox.showinfo("Game Over", self.player1.name + " won the game")
        elif self.player1.score < self.player2.score:
            messagebox.showinfo("Game Over", self.player2.name + " won the game")
        else:
            messagebox.showinfo("Game Over", "Game is a draw")

    def count_score(self, buttons):
        self.player1.score = 0
        self.player2.score = 0
        for i in range(8):
            for j in range(8):
                if buttons[i][j]["text"] == "b":
                    self.player1.score += 1
                elif buttons[i][j]["text"] == "w":
                    self.player2.score += 1

    def computer_turn(self, buttons):
        board_copy = Board.generate_2d_array(buttons)
        _, computer_row, computer_col = AlphaBeta.minimax(board_copy, self.difficulty, float("-inf"), float("inf"), True)
        if computer_row == -1 and computer_col == -1:
            print("No valid moves")
            return False
        print(computer_row, computer_col)
        Board.update_board(buttons, computer_row, computer_col, "w")
        Board.outflank(buttons, computer_row, computer_col, "w")
        return True
