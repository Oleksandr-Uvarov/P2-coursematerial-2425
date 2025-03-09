from util import Card
from util import group_by


cards = [Card("1", "spades"), Card("2", "clubs"), Card("1", "clubs"), Card("3", "hearts"), Card("4", "diamonds"), Card("queen", "clubs")]
# cards = [Card(value, suit) for value in range(2, 11) for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
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


        
def partition(xs, condition):
    true_list = []
    false_list = []

    for x in xs:
        if condition(x):
            true_list.append(x)
        else:
            false_list.append(x)

    return (true_list, false_list)

# def partition_by_color(cards):
#     black_cards, red_cards = [], []
#     for card in cards:
#         if card.suit in ("spades", "clubs"):
#             black_cards.append(card)
#         else:
#             red_cards.append(card)

#     return black_cards, red_cards

# def partition_by_color(cards):
#     # def black_suit(card):
#     #     return card.suit in ("spades", "clubs")
#     black_suit = lambda card: card.suit in ("spades", "clubs")


#     return partition(cards, black_suit)


partition_by_color = lambda cards: partition(cards, lambda card: card.suit in ("spades", "clubs"))

print(partition_by_color(cards))


