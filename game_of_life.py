 #  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def board(size):
    """Create a 3*3 matrix """
    board=[[0,1,0],[0,1,0],[0,1,0]]
    return board

def cell_alive_check(cell):
    if cell  == 1:
        return True
    else:
        return False
def all_neighbour_check(board):
    result =[[0,0,0],[0,0,0],[0,0,0]]
    for row in range(3):
        for col in range(3):
            if row ==0 and col == 0:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                result[0][0]= count
            if row ==0 and col ==1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                result[0][1]= count

            if row==0 and col==2:
                count =0
                if cell_alive_check(board[row+1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                result[0][2]= count
            if row==1 and col ==0:
                count=0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                result[1][0]= count

            if row ==1 and col ==1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col+1]):
                    count += 1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                result[1][1]= count

            if row ==1 and col ==2 :
                count =0
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                result[1][2]= count

            if row == 2 and col == 0:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                result[2][0]= count

            if row ==2 and col == 1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                result[2][1] = count

            if row == 2 and col ==2:
                count =0
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                result[2][2]= count
        
    return result

def set_rule(board, neighbour):
    for row in range(3):
        for col in range(3):
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
