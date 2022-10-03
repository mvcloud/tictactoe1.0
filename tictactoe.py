def initialize_board():
    board = []
    for row in range(3):
        sublist = []
        for col in range(3):
            sublist.append("-")  # ["-", "-", "-"]
        board.append(sublist)
    return board


def print_board(board):
    for row, sublist in enumerate(board):
        for col, cell in enumerate(sublist):
            print(board[row][col], end=" ")
        print()


def mark_square(board, row, col, player):
    if player == 1:
        board[row][col] = "x"
    else:
        board[row][col] = "o"


def is_valid(board, row, col):
    if row >= 3 or col >= 3 or row < 0 or col < 0 or board[row][col] != "-":
        return False
    return True


def check_if_winner(board, chip_type):
    # check rows
    for row in range(len(board)):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][2] == chip_type:
            return True

    # check cols
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == chip_type:
            return True

    #check diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == chip_type:
        return True

    if board[0][2] == board[1][1] and board[1][1] == board [2][0] and board[2][0] == chip_type:
        return True

    return False


def board_is_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                return False
    return True

def is_available(board, row, col):
    return board[row][col] == "-"


if __name__ == "__main__":
    print("Player 1: x\nPlayer 2: o\n")
    board = initialize_board()
    print_board(board)

    chip = "x"
    player = 1

    while True:
        print(f"\nPlayer {player}'s Turn ({chip}): ")
        row = int(input("Enter a row number (0, 1, or 2): "))
        col = int(input("Enter a column number (0, 1, or 2): "))

        while not is_valid(board, row, col):
            if row < 0 or col < 0 or row >= 3 or col >= 3:
                print("This position is off the bounds of the board! Try again.")
            else:
                print("Someone has already made a move at this position! Try again.")
            row = int(input("Enter a row number (0, 1, or 2): "))
            col = int(input("Enter a column number (0, 1, or 2): "))

        mark_square(board, row, col, player)
        print_board(board)
        if check_if_winner(board, chip) == True:
            if chip == "x":
                print("\nPlayer 1 has won!")
                break
            else:
                print("\nPlayer 2 has won!")
                break

        else:
            if board_is_full(board):
                print("It's a tie!")
                break

        player = 2 if player == 1 else 1
        chip = "o" if chip == "x" else "x"

