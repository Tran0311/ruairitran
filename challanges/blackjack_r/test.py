from classes import *
from funcs import *


def main():
    wellcome_message()
    ask_explain_rules()

    player_pot = Chips()
    game_round = True
    while game_round:
        take_bet(player_pot)
        deck, player_hand, dealer_hand = game_init()
        hit_or_stay(deck=deck, hands=(player_hand, dealer_hand))
        if player_hand.value > 21:
            player_bust(hand=player_hand, chips=player_pot)
            continue
        dealers_turn(hands=(player_hand, dealer_hand), deck=deck,
                     chips=player_pot)
        if player_pot.num_chips == 0:
            clear_screen()
            print('You Ran out of chips!')
            print('Play again soon')


if __name__ == '__main__':
    main()
