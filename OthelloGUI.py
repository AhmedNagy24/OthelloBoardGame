import time
import tkinter as tk
from GameController import *
from PIL import Image, ImageTk


class OthelloGUI:
    def __init__(self, player1_name, player2_name, difficulty):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.root.geometry("435x530")

        self.score1 = tk.IntVar(value=2)
        self.score2 = tk.IntVar(value=2)
        self.game_controller = GameController(player1_name, player2_name, difficulty)
        self.player1_name = player1_name
        self.player2_name = player2_name
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
        valid_moves = self.game_controller.generate_valid_move(self.buttons)
        self.highlight_valid_moves(valid_moves)

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
        if len(valid_moves) != 0:
            flag = False
            for (i, j) in valid_moves:
                if row == i and col == j:
                    flag = True
            if flag:
                old_turn = self.game_controller.update_board(self.buttons, row, col)
                Board.outflank(self.buttons, row, col, old_turn)
                player1_score, player2_score = self.game_controller.count_score(self.buttons)
                self.score1.set(player1_score)
                self.score2.set(player2_score)
                self.root.update()
                self.root.update_idletasks()
                check = False
                if self.player2_name == "Computer":
                    time.sleep(1)
                    check = self.game_controller.computer_turn(self.buttons)
                    if check:
                        player1_score, player2_score = self.game_controller.count_score(self.buttons)
                        self.score1.set(player1_score)
                        self.score2.set(player2_score)
                        self.root.update()
                        self.root.update_idletasks()

                print(self.game_controller.turn)
                valid_moves = self.game_controller.generate_valid_move(self.buttons)
                if len(valid_moves) == 0 and not check:
                    self.game_controller.end_game()
                    self.root.destroy()
                    import MainMenu
                    MainMenu.MainMenu().run()
                    return
                self.highlight_valid_moves(valid_moves)
                self.root.update()
                self.root.update_idletasks()
        else:
            if self.player2_name == "Computer":
                time.sleep(1)
                check = self.game_controller.computer_turn(self.buttons)
                if check:
                    player1_score, player2_score = self.game_controller.count_score(self.buttons)
                    self.score1.set(player1_score)
                    self.score2.set(player2_score)
                    self.root.update()
                    self.root.update_idletasks()
                else:
                    self.game_controller.end_game()
                    self.root.destroy()
                    import MainMenu
                    MainMenu.MainMenu().run()
                    return

    def highlight_valid_moves(self, valid_moves):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].config(background="green")
        for (i, j) in valid_moves:
            self.buttons[i][j].config(background="yellow")

    def initialize_board(self):
        white_image = Image.open("white.png")
        black_image = Image.open("black.png")
        white_image = white_image.resize((55, 55))
        black_image = black_image.resize((55, 55))
        white_photo = ImageTk.PhotoImage(white_image)
        black_photo = ImageTk.PhotoImage(black_image)
        self.buttons[3][3].config(image=white_photo, width=46, height=50, text="w")
        self.buttons[3][3].image = white_photo
        self.buttons[4][4].config(image=white_photo, width=46, height=50, text="w")
        self.buttons[4][4].image = white_photo
        self.buttons[3][4].config(image=black_photo, width=46, height=50, text="b")
        self.buttons[3][4].image = black_photo
        self.buttons[4][3].config(image=black_photo, width=46, height=50, text="b")
        self.buttons[4][3].image = black_photo

    def start(self):
        self.root.mainloop()
