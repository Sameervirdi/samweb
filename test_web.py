from web import render
from web import place_x

def test_render():
    board_data = {'a': None, 'b': None, 'c': None,
                  'd': None, 'e': None, 'f': None,
                  'g': None, 'h': None, 'i': None}

    place_x(board_data, 'e')
        
    # board_data['e'] = 'X'

    print(render(board_data))

