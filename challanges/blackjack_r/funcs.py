from classes import *


def clear_screen():
    print('\n'*100)


def wellcome_message():
    clear_screen()
    print('*'*60)
    print(''.join([' '*20, 'Wellcome To BlackJack!']))
    print('*'*60)
    print('\n'*40)
    _ = input('Press Enter to continue\n')
    clear_screen()


def ask_explain_rules():

    def rules():
        clear_screen()
        print('There are two players:')
        print('\t\t You')
        print('\t\t The Dealer')
        print('\n'*40)
        _ = input('Hit enter to continue')
        clear_screen()

        print('At the start of the game, both players are dealt two cards')
        print('\nEach card carries a value')
        print('\n\nGet the value of your hand as close as you can to 21')
        print('\n'*35)
        _ = input('Hit enter to continue')
        clear_screen()

        print('Increase the value of your card by receiving new cards \
(\'Hit\')')
        print('\n\nHowever, if the value of your hand becomes more than 21 \
you lose!')
        print('\n\n\n\n\n.... so, hit wisely')
        print('\n'*35)
        _ = input('Hit enter to continue')
        clear_screen()

        print('Once you decide to stop receiving cards, its The Dealer\'s turn\
        ')
        print('\n\nIf the value of The Dealer\'s cards are greater than \
your\'s, you loose')
        print('\n\nIf it is more than 21 or less than yours, you win!')
        print('\n'*35)
        print('Good luck!')
        _ = input('Hit enter to continue')
        clear_screen()

    clear_screen()
    print()
    print('- ' * 25)
    print('Would you like an explaination of the rules?')
    print('- ' * 25)
    print()
    print('\n'*34)
    while True:
        ans = input('Hit \'y\' or \'n\'\n')
        print('-' * 20)
        print()
        if ans.lower() not in ['y', 'n']:
            print('\n'*5)
            print('Sorry, invalid input')
            print('\n'*5)
            continue
        elif ans.lower() == 'y':
            rules()
            input('Hit enter')
            break
        else:
            break


def take_bet(chips):
    clear_screen()
    print('- ' * 35)
    print(f'You have {chips.num_chips} chips remaining')
    print('\n\nHow many chips would you like to bet on the next hand?')
    print('- ' * 35)
    print('\n' * 35)
    while True:
        ans = input('Enter a whole number\n')
        try:
            ans = int(ans)
            assert ans <= chips.num_chips
        except ValueError:
            print('Invalid Input')
            continue
        except AssertionError:
            print('You do not have enough chips for a bet of that size')
            print(f'You have {chips.num_chips} remaining')
        else:
            chips.bet_size = ans
            break


def game_init():
    deck = Deck()
    deck.shuffle()
    player_hand = Hand(owner='Player')
    player_hand.add_card(deck=deck, card=deck.deal_card())
    player_hand.add_card(deck=deck, card=deck.deal_card())

    dealer_hand = Hand(owner='Dealer')
    dealer_hand.add_card(deck=deck, card=deck.deal_card())
    dealer_hand.add_card(deck=deck, card=deck.deal_card())

    return deck, player_hand, dealer_hand


def display_hand(hand, secret=False, clear=False):
    if clear:
        clear_screen()
    else:
        print('\n' * 10)

    if not hand.owner == 'Dealer' or not secret:
        print(f'{hand.owner}\'s cards:')
        for card in hand.cards:
            print('\t' + card.__str__())
    else:
        print('Dealer\'s cards:')
        print('\t<Hidden Card>')
        print('\t' + hand.cards[1].__str__())

    if not secret:
        print('\n' * 3)
        print(f'Total value of {hand.owner}\'s cards: {hand.value}')
        print('\n' * 10)


def display_both_hands(hands, secret=True):
    player_hand, dealer_hand = hands
    clear_screen()
    display_hand(dealer_hand, clear=True, secret=secret)
    display_hand(player_hand, clear=False, secret=False)


def hit(hand, deck):
    hand.add_card(deck=deck, card=deck.deal_card())
    hand.adjust_for_aces()


def hit_or_stay(hands, deck, secret=True):
    while True:
        display_both_hands(hands, secret=secret)
        print('Would you like to hit or stay?')
        print('\n')
        ans = input('Hit \'h\' to hit and \'s\' to stay\n')
        if ans[0].lower() not in ['h', 's']:
            print('Invalid Input')
            continue
        elif ans[0].lower() == 'h':
            hit(hand=hands[0], deck=deck)
            if hands[0].value > 21:
                break
        else:
            break


def player_bust(chips, hand):
    clear_screen()
    display_hand(hand=hand)
    print('-' * 60)
    print('Player busts!!')
    print('-' * 60)
    print('\n' * 2)
    print(f'Player lost {chips.bet_size} chips')
    chips.loose_bet()
    print('\n' * 2)
    _ = input('Hit enter to continue\n')


def dealer_busts(chips, hand):
    clear_screen()
    display_hand(hand=hand, secret=False)
    print('-' * 60)
    print('Dealer busts!!')
    print('-' * 60)
    print('\n' * 2)
    print(f'Player won {chips.bet_size} chips')
    chips.win_bet()
    print('\n' * 2)
    _ = input('Hit enter to continue\n')


def dealer_wins(chips, hands):
    clear_screen()
    display_both_hands(hands, secret=False)
    print('*' * 35)
    print('Dealer Wins!')
    print(f'\n{hands[1].value} beats {hands[0].value}')
    print('*' * 35)
    print('\n' * 2)
    print(f'Player lost {chips.bet_size} chips')
    chips.loose_bet()
    print('\n' * 2)


def player_wins(chips, hands):
    clear_screen()
    display_both_hands(hands, secret=False)
    print('*' * 35)
    print('Player Wins!')
    print(f'\n{hands[0].value} beats {hands[1].value}')
    print('*' * 35)
    print('\n' * 2)
    print(f'Player won {chips.bet_size} chips')
    chips.win_bet()
    print('\n' * 2)


def draw(hands):
    clear_screen()
    display_hand(hands, secret=False)
    print('Its a draw!')


def dealers_turn(hands, deck, chips):
    clear_screen()
    print('- ' * 35)
    print('It\'s the Dealer\'s  turn now')
    print('- ' * 35)
    print('\n' * 38)
    _ = input('Press Enter to continue\n')
    while hands[1].value <= 17:
        display_both_hands(hands, secret=False)
        print('*' * 35)
        print('Dealer Hits!')
        print('*' * 35)
        print('\n' * 5)

    display_both_hands(hands, secret=False)
    print('*' * 35)
    print('Dealer Stays!')
    print('*' * 35)
    print('\n' * 5)

    if hands[1].value > 21:
        dealer_busts(chips, hands)
    elif hands[1].value > hands[0].value:
        dealer_wins(chips, hands)
    elif hands[1].value < hands[0].value:
        player_wins()
    else:
        draw()
