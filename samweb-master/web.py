"""
This is a simple webserver.

High level goals:

    Build a tic-tac-toe server

Tasks:

    * Design and implement a model for tic-tac-toe
    * Render the board to console so we can debug the state
    * Webserver listens on port 8080
    * Webserver has basic logging to stdout
    * Design a POST API that allows us to set X or O on the board

"""



"""
Design a basic Abstract Data Type (ADT) for the board



"""


board_data = {0: None, 1: None, 2: None,
              3: None, 4: None, 5: None,
              6: None, 7: None, 8: None}


def place_x(board_data, position_label):
    # TODO: implement this
    board_data[position_label] = 'X'
    pass

def place_o(board, position_label):
    # TODO: implement this
    pass

def is_occupied(board, position_label):
    # TODO: implement check if this position is already occupied
    pass


def render(board_data):
    output = """ 
    
         |      | 
     {a} |  {b} |   {c}
         |      | 
   ======+======+======
         |      |
     {d} |  {e} |   {f}
         |      |
   ======+======+======
         |      |
     {g} |  {h} |   {i}
         |      |
    """
    # TODO: walk the dictionary and set all None values
    # to the space character

    # board_data is a dictionary.

    for key in board_data.keys():
        value = board_data[key]
        # TODO: check the value, if it's None, set board_data[key] to ' '
        if value == None:
            board_data[key] = '   '
        elif value == 'X':
            board_data[key] = ' X '
        elif value == 'O':
            board_data[key] = ' O '

    return output.format(**board_data)



