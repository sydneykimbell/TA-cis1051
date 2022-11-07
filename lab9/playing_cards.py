'''
module to create a shuffle a deck of cards.
'''

import random

def get_card_color_from_suit(suit):
    '''
    Given a string representing a card suit
    return the color of the card (red or black).
    '''
    if suit == 'Spades' or suit == 'Clubs':
        return 'black'
    else:
        return 'red'


def get_card_face_from_value(value):
    '''
    Given an integer representing a card value
    return the card face (2 through A).
    '''
    if value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'
    else:
        return 'A'


def build_deck():
    '''
    Create a list representing a deck of cards. Each
    item in the list is a dictionary representing a single card.
    '''
    deck = []
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = range(2, 15)
    for suit in suits:
        for value in values:
            card = {}
            card['value'] = value
            card['suit'] = suit
            card['face'] = get_card_face_from_value(value)
            card['color'] = get_card_color_from_suit(suit)
            deck.append(card)

    return deck


def shuffle(deck):
    '''
    Implement the Fischer-Yates Shuffle to shuffle the cards.
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    '''
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def main():
    deck = build_deck()
    shuffle(deck)
    for card in deck:
        print(card)


if __name__ == '__main__':
    main()
