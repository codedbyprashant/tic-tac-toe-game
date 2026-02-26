# Tic Tac Toe Game in Python

import random

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def play_game():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        game_over = False

        while not game_over:
            print_board(board)
            row = int(input(f'Player {current_player}, enter your move (row 0-2): '))
            col = int(input(f'Player {current_player}, enter your move (col 0-2): '))

            if board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f'Player {current_player} wins!')
                    game_over = True
                elif is_board_full(board):
                    print_board(board)
                    print('The game is a tie!')
                    game_over = True
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print('Cell already taken, try again.')

        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    play_game()