# Implementing a Tic-Tac-Toe Game

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize the board
        self.current_turn = 'X'
        self.winner = None
        self.reset_game()  # reset game to initialize game variables

    def reset_game(self):
        self.board = [' ' for _ in range(9)]  # Reset board
        self.current_turn = 'X'
        self.winner = None

    # Additional game methods go here...
    
# Additional code for gameplay...