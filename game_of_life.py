#  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
import time

def board(size):
    """Create a 3*3 matrix """
    board=[[0,1,0],[0,1,0],[0,1,0]]
    return board

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
            if cell_alive_check(board[next_row][next_col]):
                count = count + 1
    return count

def set_rule(board, neighbour):
    size =3
    for row in range(size):
        for col in range(size):
            if cell_alive_check(board[row][col]):
                if neighbour[row][col] < 2:
                    board[row][col] = 0
                if neighbour[row][col] == 2 or neighbour[row][col] == 3:
                    board[row][col] = 1
                if neighbour[row][col] > 3:
                    board[row][col] = 0
            else:
                if neighbour[row][col] == 3:
                    board[row][col] = 1

    return board

def 


def display(board):
    size = size(baord)
    for row in range(size):
        for col in range(size):
            if cell_alive_check(board[row][col]):
                print(" 1 ", end=' ')
            else:
                print(" 0 ", end=' ')
        print("\n")

def main(board):
    board = [[0,1,0],[0,1,0],[0,1,0]]
    for i in range(10):
        print(f"\n{i} Generation")
        time.sleep(1)
        display(board)
        a=  set_rule(board,neighbour_check(board,row,col))
    return a 
    
    
if __name__ == "__main__":
    main(board)
        

        
