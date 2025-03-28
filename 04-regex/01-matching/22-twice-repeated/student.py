import re

def twice_repeated(string):
    return re.findall(r"(.)\1", string)