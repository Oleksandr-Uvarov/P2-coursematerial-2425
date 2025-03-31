import re
def thrice_repeated(string):
    if string == "":
        return False
    return re.fullmatch(r"(.*)\1\1", string)