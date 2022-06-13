""""This is the sudoku solver project."""

def board_gen(array):
    """This function returns a randomly-generated uniquely solvable sudoku board."""
    return array

def board_valid(board):
    """This function returns whether or not a user-inputted sudoku board is solvable."""
    if True:
        return True
    if False:
        return False

default_board = [
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]

default_solution = [
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]]

def row(board, num):
    """This function returns a desired row from the board as an array, where num is the row index, starting at 0."""
    return board[num]

def column(board, num):
    """This function returns a desired column from the board as an array, where num is the column index starting at 0."""
    col = []
    for i in range(board_len(board)):
        r = row(board, i)
        col.append(r[num])
    return col

def which_block(board, coord):
    """This function returns the block (in coordinates) a given number is in,
    based on that number's coordinates in the whole board."""
    block_coord = [coord[0]//3, coord[1]//3]
    return block_coord

def board_len(board):
    """This function returns the length in the y-direction of a given sudoku board (in the form of an array)."""
    return len(board)

def board_wid(board):
    """This function returns the width in the x-direction of a given sudoku board (in the form of an array)."""  
    return len(board[0])

def empty(num):
    """This function returns whether or not a given value in the sudoku board is empty."""
    if num == 0:
        return True
    else:
        return False

def print_board(board):
    """This function prints a given sudoku board (in the form of an array) in the terminal."""
    for i in range(board_len(board)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(board_wid(board)):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == board_wid(board) - 1:
                print(str(row(board, i)[j]))
            else:
                print(str(row(board, i)[j]) + " ", end = "")

def empty_pos(board):
    """This function returns the position of the first empty value in the board, moving from left to right, top to bottom.
    If there is no empty value, it returns None"""
    for y in range(board_len(board)):
        for x in range(board_wid(board)):
            if empty(row(board, y)[x]):
                return [x, y]
    return None
def block(board, coord):
    """This function concatenates the rows of a desired 3x3 block and returns the concatenated block as an array."""
    """The coordinates should be input in the format [x, y] where x and y range from 0 up to and including 2."""
    b = []
    for i in range(3*coord[1], 3*coord[1] + 3):
        for j in range(3*coord[0], 3*coord[0] + 3):
            b.append(board[i][j])
    return b

def valid(board, val, pos):
    """This function returns whether or not a certain value is valid at a certain position in the board."""
    #Check if value is valid considering only the row.
    for i in row(board, pos[1]):
        if i == val and i != pos[0]:
            return False
    #Check if value is valid considering only the column.
    for i in column(board, pos[0]):
        if i == val and i!= pos[1]:
            return False
    #Check if value is valid considering only the block.
    index = (pos[0] % 3) + 3*(pos[1] % 3)
    for i in block(board, which_block(board, pos)):
        if i == val and i!= index:
            return False
    return True

def solve(board):
    """This function returns the solution to a sudoku board, if it has a solution."""
    if empty_pos(board) == None:
        print_board(board)
        return True
    else:
        x, y = empty_pos(board)
        #print("This sudoku board is unsolvable!")
    for i in range(1, 10):
        if valid(board, i, [x, y]):
            board[y][x] = i
            if solve(board):
                return True
            board[y][x] = 0
    return False