import Sudoku_Solver
import flask

app = flask.Flask('__main__')

@app.route('/',methods = ['GET','POST'])
def home():
    if flask.request.method == 'GET':
        return flask.render_template('index.html',input = False)
    else:
        if '' in flask.request.form:
            # Reset the whole board
            return flask.render_template('index.html',input = False)
        else:
            num_list = []

            # Add the data from the form request to num_list
            for i in range(9):
                for j in range(9):
                    num_list.append(flask.request.form[f'{i},{j}'])
            
            # Creating the Sudoku board
            board = []
            row = []

            counter = 0
            for item in num_list:
                if item == '':
                    item = 0
                else:
                    item = int(item)

                row.append(item)
                if counter == 8:
                    board.append(row)
                    row = []
                    counter = 0
                else:
                    counter += 1
            
            game = Sudoku_Solver.SudokuGame(board)
            solution = game.Solver()
            solution_board = solution[0]
            solution_boolean = solution[1]

            for row in range(len(solution_board)):
                for column in range(len(solution_board[row])):
                    if solution_board[row][column] == 0:
                        solution_board[row][column] = ''

            return flask.render_template('index.html',input = True,solution = solution_board,solution_boolean = solution_boolean)

if __name__ == '__main__':
    app.run()