import random
import os

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Create a board
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        # We will print the board after every move
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, player):
        self.board[square] = player
        if self.winner(square, player):
            self.current_winner = player  # Set the winner

    def winner(self, square, player):
        # Check the row
        row_ind = square // 3
        if all([spot == player for spot in self.board[row_ind * 3:(row_ind + 1) * 3]]):
            return True
        # Check the column
        col_ind = square % 3
        if all([self.board[col_ind + i * 3] == player for i in range(3)]):
            return True
        # Check diagonals
        if square % 2 == 0:
            if all([self.board[i] == player for i in [0, 4, 8]]) or all([self.board[i] == player for i in [2, 4, 6]]):
                return True
        return False

    def play_game(self, mode, difficulty):
        if mode == 'PvP':
            self.play_pvp()
        elif mode == 'PvBot':
            self.play_pvbot(difficulty)

    def play_pvp(self):
        current_player = 'X'
        while self.empty_squares():
            if current_player == 'X':
                square = int(input('Player X, choose a square (0-8): '))
            else:
                square = int(input('Player O, choose a square (0-8): '))
            if self.board[square] == ' ':
                self.make_move(square, current_player)
                self.print_board()
                if self.current_winner:
                    print(f'{current_player} wins!')
                    return
                current_player = 'O' if current_player == 'X' else 'X'
        print('It’s a tie!')

    def play_pvbot(self, difficulty):
        current_player = 'X'
        while self.empty_squares():
            if current_player == 'X':
                square = int(input('Player X, choose a square (0-8): '))
                if self.board[square] == ' ':
                    self.make_move(square, current_player)
                    if self.current_winner:
                        self.print_board()
                        print('Player X wins!')
                        return
                    current_player = 'O'
            else:
                if difficulty == 'Easy':
                    square = random.choice(self.available_moves())
                elif difficulty == 'Medium':
                    square = self.medium_ai()
                else:
                    square = self.hard_ai()
                self.make_move(square, current_player)
                print(f'Bot chose square {square}.')
                self.print_board()
                if self.current_winner:
                    print('Bot wins!')
                    return
                current_player = 'X'
        print('It’s a tie!')

    def medium_ai(self):
        # Implement medium AI logic
        return random.choice(self.available_moves())

    def hard_ai(self):
        # Implement hard AI logic
        return random.choice(self.available_moves())  # Placeholder

if __name__ == '__main__':
    game = TicTacToe()
    mode = input('Choose Game Mode - Player vs Player (PvP) or Player vs Bot (PvBot): ')
    if mode == 'PvBot':
        difficulty = input('Choose difficulty level (Easy, Medium, Hard): ')
    else:
        difficulty = None
    game.play_game(mode, difficulty)