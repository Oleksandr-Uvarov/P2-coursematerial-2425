import re

def contains_three_digits(string):
    # return re.fullmatch("[0123456789]{3,}", string)
    return re.fullmatch(".*[0-9].*[0-9].*[0-9].*", string)
