from playing_cards import *

def is_high_card(deck):
    '''no cards with matching faces, and the cards do not increase in value (no straight) and do not have a matching suit (no flush)'''
    return

def is_pair(deck):
    '''exactly 2 cards of the same value'''
    return


def is_2_pair(deck):
    '''one set of 2 cards with a common value and a second set of 2 cards with a different common value'''
    return


def is_3_of_a_kind(deck):
    '''exactly 3 cards with a common value'''
    return


def is_4_of_a_kind(deck):
    '''exactly 4 cards with a common value'''
    return

def is_full_house(deck):
    '''3 cards with a common value and the other cards share a different common value'''
    return

def is_flush(deck):
    '''all 5 cards have the same suit'''
    return

def is_straight(deck):
    '''5 cards form a sequence which increases by 1 in each case'''
    return

def is_straight_flush(deck):
    '''5 cards form a sequence which increases by 1 in each case and all cards have the same suit'''
    return

def main():
    deck = build_deck()
    shuffle(deck)
    deck = deck[0:5]
    for card in deck:
        print(card)



if __name__ == '__main__':
    main()
