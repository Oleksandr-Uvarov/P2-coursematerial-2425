import re

def ababa(string):
    if string == "":
        return False
    return re.fullmatch(r"(.+)(.+)\1\2\1", string)

print(ababa("aabbaabbaa"))

print(re.fullmatch(r'(.)\1', "qq"))