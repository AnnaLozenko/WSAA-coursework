# Assignment 2: Card Draw Simulation
# Author: Anna Lozenko

import requests

def draw_and_check_hand(card_count=5):
    """
    Draws a specified number of cards from a shuffled deck and checks for pairs, triples,
    four of a kind, flush, and straight.
    :param card_count:
    :return: None
    """
    # Shuffle a new deck
    url_shuffle = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url_shuffle)
    deck_id = response.json()['deck_id']

    # Draw cards
    url_draw = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={card_count}"
    response = requests.get(url_draw)
    cards = response.json()['cards']

    # Print drawn cards
    for card in cards:
        print(f"{card['value']} of {card['suit']}")

    # Count values and suits
    value_count = {}
    suit_count = {}

    for card in cards:
        value = card['value']
        suit = card['suit']
        value_count[value] = value_count.get(value, 0) + 1
        suit_count[suit] = suit_count.get(suit, 0) + 1

    # Check for pairs, triples, four of a kind
    for count in value_count.values():
        if count == 2:
            print("Congratulations! You have drawn a pair!")
        elif count == 3:
            print("Congratulations! You have drawn a triple!")
        elif count == 4:
            print("Congratulations! You have drawn four of a kind!")

    # Check for flush (same suit)
    if 5 in suit_count.values():
        print("Congratulations! You have drawn all cards of the same suit!")

    # Check for straight
    # Step 1: value_order contains all card values in ascending order
    value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
    # Step 2: drawn_values contains all card values that have been drawn from the API
    drawn_values = [card['value'] for card in cards]
    '''
     Step 3: drawn_indices contains index of each drawn card inside value_order array, in sorted ascending order
     Examples:
     * drawn_values = [ 5, 8, QUEEN, KING, ACE ]      --> drawn_indices = [ 3, 6, 10, 11, 12 ]
     * drawn_values = [ 10, JACK, QUEEN, KING, ACE ]  --> drawn_indices = [ 8, 9, 10, 11, 12 ]
    '''
    drawn_indices = sorted(value_order.index(value) for value in drawn_values)

     # Step 4: check if all indicies in drawn_values are consecutive and in ascending order. If true, then we have a straight
    is_straight = all(
        drawn_indices[i] + 1 == drawn_indices[i + 1]
        for i in range(len(drawn_indices) - 1)
    )

    if is_straight:
        print("Congratulations! You have drawn a straight!")

draw_and_check_hand()
