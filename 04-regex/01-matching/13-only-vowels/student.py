import re

def only_vowels(string):
    return re.fullmatch("(a|o|e|i|u)*", string)