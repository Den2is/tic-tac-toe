def print_board(grid):
    """Print the tic-tac-toe board.
    """

    print("_"*13)
    print("|   |   |   |")
    print(f"| {grid[0][0]} | {grid[0][1]} | {grid[0][2]} |")
    print("|___|___|___|")
    print("|   |   |   |")
    print(f"| {grid[1][0]} | {grid[1][1]} | {grid[1][2]} |")
    print("|___|___|___|")
    print("|   |   |   |")
    print(f"| {grid[2][0]} | {grid[2][1]} | {grid[2][2]} |")
    print("|___|___|___|")


def is_winner(grid, player):
    """checking if there's a winner
    """
    #rows winner
    for row in grid:
        if row.count(player) == 3 and row[0] != '-':
            return True

    #column winner
    for row in range(len(grid)):
        aux = []
        for col in range(len(grid)):
            aux.append(grid[col][row])

        if aux.count(player) == 3 and aux[0] != '-':
            return True

    #first Diagonal winner
    aux = []
    for i in range(len(grid)):
        aux.append(grid[i][i])
    
    if aux.count(player) == 3 and aux[0] != '-':
        return True
    
    #second Diagonal winner
    aux = []
    diag = {0:2,1:1,2:0}
    for i, j in diag.items():
        aux.append(grid[i][j])

    if aux.count(player) == 3 and aux[0] != '-':
        return True


def valid_move(grid, row, col):
    """If the move of the Player is valid or not.
    """

    if grid[row][col] == '-':
        return True
    else:
        return False


def get_coordinates():
    """getting the moves
    firs digit is the rows value
    second digit is the columns value
    """

    while True:
        move = input("Type the row/col value: ")

        if len(move) < 2 or len(move) > 2 or not move:
            print("You lost the move.")
            return None, None

        if move.isdigit():
            move = list(move)
            row = int(move[0])
            col = int(move[1])
            return row, col


def run():
    
    grid = [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]

    print("TIC TAC TOE")
    try:
        while True:

            print_board(grid)

            row, col = get_coordinates()

            if not row or not col:
                continue

            char = input("X/O ").upper()

            if valid_move(grid, row, col):
                grid[row][col] = char

                if is_winner(grid, char):
                    print_board(grid)
                    print(f"Player {char} have won!!!")
                    break

            else:
                print(f"{char} palyer have lost the move")
                continue

    except KeyboardInterrupt:
        print("\nSee you soon!!!")


if __name__ == '__main__':
    run()
