#test_game_of _life
import game_of_life

def test_matrix():
    actual_result = ([[0,1,0],[0,1,0],[0,1,0]])
    assert game_of_life.board(3) == actual_result
