import tkinter as tk
from OthelloGUI import OthelloGUI


class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Menu")
        self.root.geometry("495x350")
        self.title = tk.Label(self.root, text="Othello", font=("Arial", 24, "bold"))
        self.title.grid(row=0, column=1, columnspan=3)
        self.blank_label = tk.Label(self.root, text="", font=("Arial", 16), width=5)
        self.blank_label.grid(row=0, column=0)
        self.player1_label = tk.Label(self.root, text="Player 1", font=("Arial", 16))
        self.player1_label.grid(row=1, column=1, padx=10, pady=10)
        self.player1_entry = tk.Entry(self.root, font=("Arial", 16))
        self.player1_entry.grid(row=1, column=2, pady=10)
        self.player2_label = tk.Label(self.root, text="Player 2", font=("Arial", 16))
        self.player2_label.grid(row=2, column=1, padx=10)
        self.player2_entry = tk.Entry(self.root, font=("Arial", 16))
        self.player2_entry.grid(row=2, column=2)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=3, column=2, columnspan=2)
        self.comp_label = tk.Label(button_frame, text="Computer", font=("Arial", 16))
        self.comp_label.grid(row=0, column=1, padx=0, pady=10)
        self.comp_var = tk.IntVar()
        self.comp_check = tk.Checkbutton(button_frame, variable=self.comp_var, command=self.computer)
        self.comp_check.grid(row=0, column=0, padx=0, pady=10)
        self.difficulty_label = tk.Label(button_frame, text="Difficulty", font=("Arial", 16))
        self.difficulty_label.grid(row=1, column=0, columnspan=3)
        self.diff_value = tk.IntVar(value=1)
        self.diff_radio1 = tk.Radiobutton(button_frame, text="Easy", font=("Arial", 16), variable=self.diff_value, value=1, state="disabled")
        self.diff_radio1.grid(row=2, column=0, pady=10)
        self.diff_radio2 = tk.Radiobutton(button_frame, text="Medium", font=("Arial", 16), variable=self.diff_value, value=5, state="disabled")
        self.diff_radio2.grid(row=2, column=1, pady=10)
        self.diff_radio3 = tk.Radiobutton(button_frame, text="Hard", font=("Arial", 16), variable=self.diff_value, value=15, state="disabled")
        self.diff_radio3.grid(row=2, column=2, pady=10)
        self.start_button = tk.Button(button_frame, text="Start", font=("Arial", 16), command=self.start)
        self.start_button.grid(row=3, column=0)
        self.quit_button = tk.Button(button_frame, text="Quit", font=("Arial", 16), command=self.quit)
        self.quit_button.grid(row=3, column=1)

    def computer(self):
        if self.comp_var.get() == 1:
            self.player2_entry.config(state="disabled")
            self.diff_radio1.config(state="normal")
            self.diff_radio2.config(state="normal")
            self.diff_radio3.config(state="normal")
        else:
            self.player2_entry.config(state="normal")
            self.diff_radio1.config(state="disabled")
            self.diff_radio2.config(state="disabled")
            self.diff_radio3.config(state="disabled")

    def start(self):
        player1 = self.player1_entry.get()
        player2 = self.player2_entry.get()
        if player1 == "":
            player1 = "Player 1"
        if player2 == "":
            player2 = "Player 2"
        self.root.destroy()
        if self.comp_var.get() == 1:
            player2 = "Computer"
        game = OthelloGUI(player1, player2, self.comp_var.get(), self.diff_value.get())
        game.start()

    def quit(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
