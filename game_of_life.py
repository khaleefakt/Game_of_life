#  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def board(size):
    """Create a 3*3 matrix """
    board=[[0,1,0],[0,1,0],[0,1,0]]
    return board


def cell_alive_check(cell):
    #Check whether the cell is active or not 
    #cell = board(3)
    if cell  == 1:
        return True
    else:
        return False

"""def make_alive(board, row, col):
    live_cell = board()
    cell = cell_alive_check()
    r_1 = 
    for i in row:
        for j in col:
            if cell == 1:
                set cell == 0"""
                
