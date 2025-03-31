import re

def twice_repeated(string):
    if string == "":
        return False
    return re.fullmatch(r"(.*)\1", string)


print(bool(twice_repeated("")))