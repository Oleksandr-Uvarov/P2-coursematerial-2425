from util import Card
from util import group_by

cards = [Card("1", "Spades"), Card("2", "Clubs"), Card("1", "Clubs"), Card("3", "Hearts"), Card("4", "Diamonds"), Card("Queen", "Clubs")]
# group_by_suit = lambda card: (card.suit, card.value)

# group_by_value = lambda card: (card.value, card.suit)


# print(sorted(cards, key=group_by_suit))
# print(sorted(cards, key=group_by_value))

# print(sorted(cards, key=group_by(group_by_suit)))

# group_by_suit = lambda cards: group_by(cards, card.suit)
# group_by_suit = group_by(cards, lambda card: card.suit)
# group_by_value = lambda card: group_by(cards, card.value)

# def group_by_suit(cards):
#     card_dict = {}
#     for card in cards:
#         if card.suit not in card_dict:
#             card_dict[card.suit] = []
#         card_dict[card.suit].append(card.value)
#     return card_dict


# print(group_by_suit(cards))
# print(group_by(cards, lambda card : card.value))
# print(group_by(cards, lambda card : card.suit))

group_by_value = lambda cards: group_by(cards, lambda card: card.value)
group_by_suit = lambda cards: group_by(cards, lambda card: card.suit)


        


def partition_by_color(cards):
    black_cards, red_cards = [], []
    for card in cards:
        if card.suit in ("Spades, Clubs"):
            black_cards.append(card)
        else:
            red_cards.append(card)

    return black_cards, red_cards
    # return red_cards, black_cards

# partition_by_color = lambda card: [[card.suit in ("Spades, Clubs")], [card.suit in ("Hearts, Diamonds")]]