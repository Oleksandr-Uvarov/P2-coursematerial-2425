def count(xs, predicate):
    return len([x for x in xs if predicate(x)])


def indices_of(xs, condition):
    return [index for index in range(len(xs)) if condition(xs[index])]

def count_older_than(people, min_age):
    def older_than_min_age(person):
            return person.age >= min_age
        
    return count(people, older_than_min_age)


def indices_of_cards_with_suit(cards, suit):
    def of_suit(card):
        return card.suit == suit
    
    return indices_of(cards, of_suit)