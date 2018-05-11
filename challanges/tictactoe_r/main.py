import tic_tac as tt


def greeting():
    print('\nHello!\nWelcome to Xs and Os')
    print('\n' * 3)
    board = [' '] * 10
    return board


def get_names():
    name_1 = input('Player 1, what is your name?\n')
    print()
    name_2 = input('Player 2, what is your name?\n')
    print()
    names = (name_1, name_2)
    player_1 = names[int(tt.choose_first())]
    player_2 = names[0] if names[0] != player_1 else names[1]
    print(f'{player_1}, You will go first')
    return (player_1, player_2)


def explain_choosing():
    print('\n' * 3)
    print('Use a number to pick a position\nSee the key below:')
    tt.display_board(list(map(str, range(10))), explainer=True)


def main():
    board = greeting()
    winner = False
    player_switch_counter = 0

    player_1, player_2 = get_names()
    m_player_1 = tt.player_input()
    m_player_2 = 'X' if m_player_1 != 'X' else 'O'

    player_info = list(zip([player_1, player_2], [m_player_1, m_player_2]))
    while True:  # game loop
        while True:
            current_player, current_marker = \
                player_info[player_switch_counter % 2]
            if player_switch_counter != 0:
                print(f'{current_player} it is your go\n\nReminder, you are \
                      {current_marker}')

            explain_choosing()
            tt.display_board(board)
            chosen_position = tt.player_choice(board)
            board = tt.place_marker(board, current_marker, chosen_position)
            tt.display_board(board)

            if tt.win_check(board, current_marker):
                winner = True
                break
            if ' ' not in board[1:]:
                break

            player_switch_counter += 1

        if winner:
            print(f'{current_marker} won!\nCongratulations {current_player}!')
        else:
            print('its a draw!')

        if not tt.replay():
            break


if __name__ == '__main__':
    main()
