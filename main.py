import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.reset_game()

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        self.play_again_button = tk.Button(self.master, text="Play Again", font=("Arial", 20), command=self.reset_game)
        self.play_again_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.play_again()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.play_again()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def play_again(self):
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()