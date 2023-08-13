def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    print("Welcome to Tic Tac Toe!\n")
    print("In this game, two players take turns to place their marks (X or O) on a 3x3 grid.\n")
    print("The goal is to be the first to get three of their marks in a row, column, or diagonal.\n")
    print("Let's get started!\n")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["1", "2"]
    current_player = 0

    print_board(board)

    while True:
        row = int(input(f"Player {players[current_player]}, enter row (up-down, 0-2): "))
        col = int(input(f"Player {players[current_player]}, enter column (left-right, 0-2): "))
        
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)

                if check_winner(board, players[current_player]):
                    print(f"Player {players[current_player]} wins!")
                    break
                elif is_full(board):
                    print("It's a draw!")
                    break

                current_player = 1 - current_player
            else:
                print("That cell is already taken. Try again.")
        else:
            print("Invalid input. Row and column must be between 0 and 2.")

if __name__ == "__main__":
    main()
