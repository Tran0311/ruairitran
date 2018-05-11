import random


def display_board(board, explainer=False):
    '''
    This function prints a board

    Parameters:
        board: the board to be printed

    Returns:
        Nothing
    '''

    print('\n')
    if not explainer:
        print('This is the Curernt board: \n')
    for line in range(1, 10, 3):
        print('|'.join([board[line], board[line+1], board[line+2]]))


def player_input():
    '''
    This function asks the user for their marker
    It keeps on asking until the user enters an x or an o

    Parameters:
        Nothing

    Returns:
        marker: the chosen marker

    '''

    while True:
        marker = input('Choose a marker: X or O     ').upper()
        if marker in ['X', 'O']:
            break
    return marker


def place_marker(board, marker, position):
    '''
    Given a position to fill, this function updates the board with
    the appropriate marker

    Parameters:
        board: the board to update
        marker: the marker to use
        position: the position to fill in with the marker

    Returns:
        board: the updated board

    '''

    board[position] = marker
    return board


def win_check(board, mark):
    '''
    Given a board, this function checks to see if a marker has won

    Parameters:
        board: the board to check
        mark: the marker to check

    Returns:
        Bool: True if marker has one; False if not

    '''

    win_cases = [board[1:4],
                 board[4:7],
                 board[7:],
                 [board[1], board[5], board[9]],
                 [board[7], board[5], board[3]],
                 [board[1], board[4], board[7]],
                 [board[2], board[5], board[8]],
                 [board[3], board[6], board[9]]
                 ]

    for win_case in win_cases:
        if mark*3 in ''.join(win_case):
            return True
    else:
        return False


def choose_first():
    '''
    This function randomly selects one of two players

    Parameters:
        None

    Returns:
        '1' or '2'

    '''

    return str(random.randint(0, 1))


def space_check(board, position):
    '''
    This function checks whether there is space on the board
    at a given position

    Parameters:
        board: the board to check
        position: the position to check

    Returns:
        Bool: True if there is space on the board; False if not

    '''

    return board[position] == ' '


def player_choice(board):
    '''
    This function prompts the user for a position
    It continues to do so until the user enters a valid position

    Parameters:
        board: the board in game use

    Returns:
        the selected position (int)

    '''

    while True:
        position_to_check = input('Choose a position: ')

        if position_to_check not in map(str, range(1, 10)):
            continue
        else:
            position_to_check = int(position_to_check)

        if space_check(board, position_to_check):
            break
        else:
            print('That position is already in use!')

    return position_to_check


def replay():
    '''
    This function prompts the user whether they would like to

    '''
    while True:
        answer = input('Would you like to play again? (y/n)').lower()
        if answer in ['y', 'n']:
            break
    return answer == 'y'
