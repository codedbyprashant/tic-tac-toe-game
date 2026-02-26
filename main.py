import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe - AI Game")
        master.geometry("500x600")
        master.configure(bg='#f0f0f0')
        
        # Initialize game variables first
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.buttons = []
        
        # Title
        title = tk.Label(master, text="Tic Tac Toe", font=('Arial', 24, 'bold'), bg='#f0f0f0')
        title.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Create buttons for the board
        self.buttons = [[tk.Button(master, text="", font=('Arial', 20, 'bold'), 
                                    width=6, height=3, bg='white',
                                    command=lambda row=i, col=j: self.make_move(row, col))
                         for j in range(3)] for i in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)
        
        # Difficulty selection
        difficulty_frame = tk.Frame(master, bg='#f0f0f0')
        difficulty_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        tk.Label(difficulty_frame, text="AI Difficulty:", font=('Arial', 12), bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        self.difficulty = tk.StringVar(value="Easy")
        difficulty_menu = tk.OptionMenu(difficulty_frame, self.difficulty, "Easy", "Medium", "Hard")
        difficulty_menu.pack(side=tk.LEFT, padx=5)
        
        # Game mode selection
        mode_frame = tk.Frame(master, bg='#f0f0f0')
        mode_frame.grid(row=5, column=0, columnspan=3, pady=10)
        
        tk.Label(mode_frame, text="Game Mode:", font=('Arial', 12), bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        self.mode = tk.StringVar(value="Player vs Bot")
        mode_menu = tk.OptionMenu(mode_frame, self.mode, "Player vs Player", "Player vs Bot")
        mode_menu.pack(side=tk.LEFT, padx=5)
        
        # Info label
        self.info_label = tk.Label(master, text="Turn: Player X", font=('Arial', 14), 
                                   bg='#f0f0f0', fg='#333')
        self.info_label.grid(row=6, column=0, columnspan=3, pady=10)
        
        # Restart button
        self.restart_button = tk.Button(master, text="New Game", font=('Arial', 12),
                                        command=self.reset_game, bg='#4CAF50', fg='white',
                                        padx=20, pady=10)
        self.restart_button.grid(row=7, column=0, columnspan=3, pady=10)
    
    def reset_game(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.update_display()
        
        # Update all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg='white', state=tk.NORMAL)
    
    def make_move(self, row, col):
        # Check if cell is empty and game is not over
        if self.game_over or self.board[row][col] is not None:
            return
        
        # Player's move
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)
        
        if self.check_winner(self.current_player):
            self.info_label.config(text=f"🎉 Player {self.current_player} wins!", fg='green')
            self.game_over = True
            self.disable_all_buttons()
            return
        
        if self.check_draw():
            self.info_label.config(text="🤝 It's a Draw!", fg='blue')
            self.game_over = True
            self.disable_all_buttons()
            return
        
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
        self.update_display()
        
        # AI move if playing against bot
        if self.mode.get() == "Player vs Bot" and self.current_player == "O":
            self.master.after(500, self.ai_move)
        elif self.mode.get() == "Player vs Player":
            # Continue with next player
            pass
    
    def ai_move(self):
        if self.game_over:
            return
        
        difficulty = self.difficulty.get()
        
        if difficulty == "Easy":
            row, col = self.easy_ai()
        elif difficulty == "Medium":
            row, col = self.medium_ai()
        else:  # Hard
            row, col = self.hard_ai()
        
        if row is not None and col is not None:
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state=tk.DISABLED)
            
            if self.check_winner("O"):
                self.info_label.config(text="🤖 AI wins!", fg='red')
                self.game_over = True
                self.disable_all_buttons()
                return
            
            if self.check_draw():
                self.info_label.config(text="🤝 It's a Draw!", fg='blue')
                self.game_over = True
                self.disable_all_buttons()
                return
            
            self.current_player = "X"
            self.update_display()
    
    def easy_ai(self):
        """Easy AI: Makes random valid moves"""
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if empty_cells:
            return random.choice(empty_cells)
        return None, None
    
    def medium_ai(self):
        """Medium AI: Blocks opponent wins and takes winning opportunities"""
        # Try to win
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = "O"
                    if self.check_winner("O"):
                        self.board[i][j] = None
                        return i, j
                    self.board[i][j] = None
        
        # Block opponent
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = "X"
                    if self.check_winner("X"):
                        self.board[i][j] = None
                        return i, j
                    self.board[i][j] = None
        
        # Take center if available
        if self.board[1][1] is None:
            return 1, 1
        
        # Take corners
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [(i, j) for i, j in corners if self.board[i][j] is None]
        if available_corners:
            return random.choice(available_corners)
        
        # Take any available space
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if empty_cells:
            return random.choice(empty_cells)
        
        return None, None
    
    def hard_ai(self):
        """Hard AI: Uses Minimax algorithm for optimal play"""
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = "O"
                    score = self.minimax(0, False)
                    self.board[i][j] = None
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            return best_move
        
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if empty_cells:
            return random.choice(empty_cells)
        
        return None, None
    
    def minimax(self, depth, is_maximizing):
        """Minimax algorithm for optimal AI play"""
        if self.check_winner("O"):
            return 10 - depth
        if self.check_winner("X"):
            return depth - 10
        if self.check_draw():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = "O"
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = None
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = "X"
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = None
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, player):
        """Check if a player has won"""
        # Check rows
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True
        
        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        
        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]):
            return True
        if all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        
        return False
    
    def check_draw(self):
        """Check if the game is a draw"""
        return all([self.board[i][j] is not None for i in range(3) for j in range(3)])
    
    def update_display(self):
        """Update the info label"""
        if not self.game_over:
            self.info_label.config(text=f"Turn: Player {self.current_player}", fg='#333')
    
    def disable_all_buttons(self):
        """Disable all board buttons"""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()