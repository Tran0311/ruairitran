from random import shuffle


class Card:
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Deck.suits for
                      rank in Deck.ranks]

    def __str__(self):
        out = 'Cards in the Deck:\n'
        for card in self.cards:
            out = '\n'.join([out, card.__str__()])
        return out

    def shuffle(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:

    def __init__(self, owner='NOT PROVIDED'):
        self.cards = []  # could be touple?
        self.value = 0
        self.num_aces = 0
        self.owner = owner

    def add_card(self, deck, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.num_aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.num_aces:
            self.value -= 10
            self.num_aces -= 1


class Chips:

    def __init__(self):
        self.num_chips = 100
        self.bet_size = 0

    def win_bet(self):
        self.num_chips += self.bet_size

    def loose_bet(self):
        self.num_chips -= self.bet_size
