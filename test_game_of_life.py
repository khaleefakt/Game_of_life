#test_game_of _life
import game_of_life

def test_matrix():
    actual_result = [[0,1,0],[0,1,0],[0,1,0]]
    assert game_of_life.board(3) == actual_result

def test_alive_cell():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    assert game_of_life.cell_alive(board[0],[1]) == False
    assert game_of_life.cell_alive(board[1],[1]) == False
    assert game_of_life.cell_alive(board[2],[1]) == False
