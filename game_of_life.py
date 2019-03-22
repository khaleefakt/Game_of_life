import time


def cell_alive_check(cell):
    return cell  == 1

def neighbour_check(board,row,col):
    size_limit = len(board)-1
    count = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:        
            next_row = row + i
            next_col = col +j
            if next_row == row and next_col ==col:
                continue
            if next_row <0 or next_col<0 or next_row >size_limit or next_col >size_limit:
                continue
            if board[next_row][next_col]==1:
                count = count + 1
    return count

#  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def set_rule(board):
    new_board=[[0,0,0],
               [0,0,0],
               [0,0,0]]
    row_size = len(board)
    col_size = len(board)
    for row in range(row_size):
        for col in range(col_size):
            if neighbour_check(board,row,col) < 2 and board[row][col] == 1:
                new_board[row][col] = 0
            elif neighbour_check(board,row,col) in [2,3] and board[row][col] == 1:
                new_board[row][col] = 1
            elif neighbour_check(board,row,col) > 3 and board[row][col] == 1:
                new_board[row][col]= 0
            else:
                if neighbour_check(board,row,col) == 3 and board[row][row] == 0:
                    new_board[row][col] =1

    return new_board

def display(board):
    size = len(board)
    rows = []
    for i in range(size):
        cols = []
        for j in range(size):
            if board[i][j] == 1:
                cols.append("1")
            else:
                cols.append("0")
        rows.append(" ".join(cols))
    return "\n\n".join(rows)

def main(board):
    row = len(board)
    col =len(board)
    for i in range(0,10):
        print("\n{} Generation".format(i))
        time.sleep(0.5)
        print(display(board))
        board = set_rule(board)
    time.sleep(0.5)
    
    
if __name__ == "__main__":
    board = [[0,1,0],
             [0,1,0],
             [0,1,0]]
    
    main(board)
        

        
