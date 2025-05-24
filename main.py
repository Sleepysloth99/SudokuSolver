import random
import copy


#box_index = (row // 3) * 3 + (col // 3)

#fucntion to create an empty board
def emptyBoard():
    #Initialize a 2d list in the size of 9x9.
    boardtemp = [[0 for i in range(9)] for j in range(9)]
    return boardtemp

    #for row in boardtemp:
     #   print(row)

#grid[i][j] = x
def fillinBoard(grid, values):
    for row, col, val in values:
        grid[row][col] = val
    return grid

#prints the board to console as a 9x9
def printBoard(board):
    for row in board:
        print(row)

def generateFullBoard():
    board = emptyBoard()
    fillBoard(board)
    return board

def checkNum(board, row, col, num):

    #check row
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[box_row + i][j + box_col] == num:
                return False
    return True

def fillBoard(board):
    nums = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(nums)
                for num in nums:
                    if checkNum(board, i, j, num):
                        board[i][j] = num
                        if fillBoard(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def fullBoard(board):
    full_board = emptyBoard()
    fillBoard(full_board)
    return full_board

def generatesudoku(board, num_remove=50):
    sudokupuzzle = [row[:] for row in board]
    count = 0
    while count < num_remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if sudokupuzzle[row][col] != 0:
            sudokupuzzle[row][col] = 0
            count += 1
    return sudokupuzzle

def solution(board):
    if solveBoard(board):
        print("Solution found:")
        printBoard(board)
    else:
        print("No solution found.")
    return

def solveBoard(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if checkNum(board, row, col, num):
                        board[row][col] = num
                        if solveBoard(board):
                            return True
                        board[row][col] = 0
                return False
    return True




#Initialize an empty board

empty_board = emptyBoard()
print("empty board: ")
printBoard(empty_board)
fullboard = generateFullBoard()
print("Generated full board: ")
printBoard(fullboard)
sudoku = generatesudoku(fullboard)
print("Generated sudoku puzzle: ")
printBoard(sudoku)

solution(sudoku)
