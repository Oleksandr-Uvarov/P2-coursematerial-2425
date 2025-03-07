list_of_strings = ["abc", "defg", "afgssss"]

print(sorted(list_of_strings, key=lambda string: len(string)))

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value}, {self.suit}"

list_of_cards = [Card("1", "Diamonds"), Card("Queen", "Spades"), Card("3", "Diamonds")]
        
# for this to work we need to define the __lt__
# print(sorted(list_of_cards))

print(sorted(list_of_cards, key=lambda card: card.value))


# if there are multiple values and the first value is equal, then we can use
# a tuple so that if the first number is equal, it compares the second value

print(sorted(list_of_cards, key=lambda card: (card.value, card.suit), reverse=True))