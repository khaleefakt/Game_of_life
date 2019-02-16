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

"""def test_make_alive_cell():
    board = [[0,1,0],[0,1,0][0,1,0]]
    assert game_of_life.cell.make_alive(board[1],[0]) == True
    assert game_of_life.cell.make_alive(board[1],[1]) == True
    assert game_of_life.cell.make_alive(board[1],[2]) == True"""
    
