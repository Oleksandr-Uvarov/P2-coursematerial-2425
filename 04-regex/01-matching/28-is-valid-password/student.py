import re

def is_valid_password(string):
    return re.fullmatch(r"(.*[0-9]+.*[a-z]+.*[A-Z]+.*[+|-|*|/|.|@]+.*){12,}", string)
    # return re.fullmatch("([A-Z]+.*){12,}", string)