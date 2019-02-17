#test_game_of _life

import game_of_life

def test_matrix():
    actual_result = [[0,1,0],[0,1,0],[0,1,0]]
    assert game_of_life.board(3) == actual_result

def test_check_cell_alive():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    assert game_of_life.cell_alive_check(board[0][1]) == True
    assert game_of_life.cell_alive_check(board[1][1]) == True
    assert game_of_life.cell_alive_check(board[2][1]) == True
    assert game_of_life.cell_alive_check(board[2][2]) == False


def test_all_neighbour_check():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    result = [[2,1,2],[3,2,3],[2,1,2]]
    assert game_of_life.all_neighbour_check(board) == result

    
#  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def test_rules():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    neig =  [[2,1,2],[3,2,3],[2,1,2]]
    result = [[0,0,0],[1,1,1],[0,0,0]]

    assert game_of_life.set_rule(board,neig)== result
    
