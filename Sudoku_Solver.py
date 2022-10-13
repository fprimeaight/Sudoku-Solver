# Sudoku solver
class SudokuGame:
    def __init__(self,board):
        self.size = 9
        self.board = board

    def Display(self):
        for i in range(self.size):
            output = ''
            for j in range(self.size):
                if self.board[i][j] == 0:
                    output += '-  '
                else:
                    output += f'{self.board[i][j]}  '
            print(output)

    def CheckRow(self,row,val):
        if val in self.board[row]:
            return False
        else:
            return True

    def CheckColumn(self,column,val):
        for i in range(self.size):
            if val == self.board[i][column]:
                return False
        return True

    def CheckBox(self,row,column,val):
        box_row = row // 3
        box_column = column // 3

        # Check through all the numbers in the current box
        for i in range(3):
            for j in range(3):
                curr_row = box_row * 3 + i
                curr_column = box_column * 3 + j
                if val is self.board[curr_row][curr_column]:
                    return False
        return True
                    
    def CheckSquareIsSafe(self,row,column,val):
        if self.CheckBox(row,column,val) == True and self.CheckRow(row,val) == True and self.CheckColumn(column,val) == True:
            return True
        else:
            return False

    def SearchEmptySquare(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return [i,j]
        return None

    def Solver(self):
        # Check if starting position even is legal
        for i in range(self.size):
            for j in range(self.size):
                val = self.board[i][j]
                self.board[i][j] = 0
                if val != 0 and self.CheckSquareIsSafe(i,j,val) == False:
                    self.board[i][j] = val
                    return self.board,False
                self.board[i][j] = val
                    
        if self.SolverHelper() == True:
            return self.board,True
        else:
            return self.board,False

    def SolverHelper(self):
        # Using backtracking
        if self.SearchEmptySquare() != None:
            row = self.SearchEmptySquare()[0]
            column = self.SearchEmptySquare()[1]
        
            for num in range(1,10):
                if self.CheckSquareIsSafe(row,column,num) == True:
                    # Place the new value in that position and call the function recursively again
                    self.board[row][column] = num
                    if self.SolverHelper() == True:
                        return True
                    self.board[row][column] = 0

            # If all the 9 values don't work for that square, backtrack
            return False
        else:
            return True

# Testing

# Main program
def main(board):
    game = SudokuGame(board)

    print('Initial Position: ')
    game.Display()
    print('Solution:')
    game.Solver()
    game.Display()


# Insert your board initial position here
board = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Run program
if __name__ == '__main__':
    main(board)