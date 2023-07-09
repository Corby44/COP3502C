# 3502C Lab 5 Code
# Written by: Michael Muraglia
# 7/2/20233

def print_board(board):
    for row in board[::-1]:  # prints the board in opposite order as it is stored
        for col in row:
            print(col, end=" ")
        print()
    print()


def initialize_board(num_rows, num_cols):  # initializes the board with all '-' an indicated dimensions
    board = []
    for row in range(num_rows):
        row = []
        for col in range(num_cols):
            row.append('-')
        board.append(row)
    return board


def insert_chip(board, col, chip_type):  # inserts the player 1 or player 2's token in desired location
    row_index = 0  # Initializes row index variable
    for row in board:
        if row[col] == '-':
            row[col] = chip_type
            break
        else:
            row_index += 1  # decrements row index variable
            continue
    return row_index


def check_if_winner(board, col, row, chip_type):
    tie_counter = len(board[-1])  # number of columns of board - helps determine if tie has been reached
    win_counter = 0  # keeps track of how many like tokens are in a row - determines if last move won game
    return_value = False  # value returned to function to indicated game has been won/tied/or continues

    for column in board[-1]:  # gets last low in board (top row)
        if column == '-':  # game continues if - present in top row
            break
        else:
            tie_counter -= 1  # counter helps determine if at last column
            if tie_counter == 0:  # 0 indicates last column
                print('Draw. Nobody wins.')
                return_value = True
            else:
                continue

    if not return_value:
        for column in board[row]:  # Determines if horizontal connect four
            if column == chip_type:
                win_counter += 1
                if win_counter == 4:
                    if chip_type == 'x':
                        print('Player 1 won the game!')
                        return_value = True
                    else:
                        print("Player 2 won the game!")
                        return_value = True
            else:
                win_counter = 0

    win_counter = 0
    if not return_value:
        for row in board:  # Determines if vertical connect four
            if row[col] == chip_type:
                win_counter += 1
                if win_counter == 4:
                    if chip_type == 'x':
                        print('Player 1 won the game!')
                        return_value = True
                    else:
                        print("Player 2 won the game!")
                        return_value = True
            else:
                win_counter = 0

    return return_value


def main():
    n_rows = int(input("What would you like the height of the board to be? "))  # prompts for user dimensions of board
    n_cols = int(input("What would you like the length of the board to be? "))

    board = initialize_board(n_rows, n_cols) # initializes board
    print_board(board)  # prints board

    print("Player 1: x")  # indicates player 1 and player 2 tokens
    print("Player 2: o\n")

    while True:
        choice = int(input("Player 1: Which column would you like to choose? "))  # player 1's move choice
        token = 'x'
        row_index = insert_chip(board, choice, token)
        print_board(board)
        return_value = check_if_winner(board, choice, row_index, token)
        if return_value:
            break

        choice = int(input("Player 2: Which column would you like to choose? ")) # player 2's move choice
        token = 'o'
        row_index = insert_chip(board, choice, token)
        print_board(board)
        return_value = check_if_winner(board, choice, row_index, token)
        if return_value:
            break


if __name__ == "__main__":
    main()
