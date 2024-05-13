import time
import tkinter as tk
from GameController import *


class OthelloGUI:
    def __init__(self, player1_name, player2_name, isComp, difficulty):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.root.geometry("435x530")

        self.score1 = tk.IntVar(value=2)
        self.score2 = tk.IntVar(value=2)
        self.game_controller = GameController(player1_name, player2_name, isComp, difficulty)
        self.buttons = []
        self.draw_board()
        self.initialize_board()
        self.black_label = tk.Label(self.root, text=player1_name, font=("Arial", 16, "bold"))
        self.black_label.grid(row=0, column=0, columnspan=4)
        self.white_label = tk.Label(self.root, text=player2_name, font=("Arial", 16, "bold"))
        self.white_label.grid(row=0, column=4, columnspan=4)
        self.black_score = tk.Label(self.root, textvariable=self.score1, font=("Arial", 16), padx=10)
        self.black_score.grid(row=1, column=0, columnspan=4)
        self.white_score = tk.Label(self.root, textvariable=self.score2, font=("Arial", 16), padx=10)
        self.white_score.grid(row=1, column=4, columnspan=4)

    def draw_board(self):
        for i in range(8):
            row_buttons = []
            for j in range(8):
                button = tk.Button(self.root, width=6, height=3,
                                   command=lambda row=i, col=j: self.button_click(row, col),
                                   background="green", activebackground="green", borderwidth=3, text="")
                button.grid(row=i + 2, column=j, sticky="nsew")
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def button_click(self, row, col):
        valid_moves = self.game_controller.generate_valid_move(self.buttons)
        self.highlight_valid_moves(valid_moves)
        flag = valid_moves.count((row, col))
        if flag > 0:
            old_turn = self.game_controller.update_board(self.buttons, row, col)
            Board.outflank(self.buttons, row, col, old_turn)
            check = False
            if self.game_controller.player2.isComputer:
                # time.sleep(1)
                check = self.game_controller.computer_turn(self.buttons)

            self.update_gui()
            valid_moves = self.game_controller.generate_valid_move(self.buttons)
            if len(valid_moves) == 0 and not check:
                self.end()
                return
            elif len(valid_moves) == 0 and check:
                valid_moves = self.game_controller.generate_valid_move(self.buttons)
                while len(valid_moves) == 0 and check:
                    check = self.game_controller.computer_turn(self.buttons)
                    self.update_gui()
                    valid_moves = self.game_controller.generate_valid_move(self.buttons)
                valid_moves = self.game_controller.generate_valid_move(self.buttons)
                if len(valid_moves) == 0 and not check:
                    self.end()
                    return
            self.highlight_valid_moves(valid_moves)
            self.root.update()
            self.root.update_idletasks()

    def highlight_valid_moves(self, valid_moves):
        for i in range(8):
            for j in range(8):
                if self.buttons[i][j]["background"] != "black" and self.buttons[i][j]["background"] != "white":
                    self.buttons[i][j].config(background="green")
        for (i, j) in valid_moves:
            self.buttons[i][j].config(background="yellow")

    def initialize_board(self):
        Board.update_board(self.buttons, 3, 3, "w")
        Board.update_board(self.buttons, 4, 4, "w")
        Board.update_board(self.buttons, 3, 4, "b")
        Board.update_board(self.buttons, 4, 3, "b")
        valid_moves = self.game_controller.generate_valid_move(self.buttons)
        self.highlight_valid_moves(valid_moves)

    def update_gui(self):
        self.game_controller.count_score(self.buttons)
        self.score1.set(self.game_controller.player1.score)
        self.score2.set(self.game_controller.player2.score)
        self.root.update()
        self.root.update_idletasks()

    def start(self):
        self.root.mainloop()

    def end(self):
        self.game_controller.end_game()
        self.root.destroy()
        import MainMenu
        MainMenu.MainMenu().run()
        return
