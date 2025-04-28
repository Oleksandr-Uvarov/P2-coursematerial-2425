import re

def remove_trailing_whitespace(string):
    # return re.sub(r".+' '$", "", string, re.MULTILINE)
    # return re.sub(r"(' ').+$", "", string, re.MULTILINE)
    return re.sub(r"[' '|\t]+$", "", string, flags=re.MULTILINE)


# print(remove_trailing_whitespace("fdjfkld jfjs fjdslfk       ") + "1")
print(remove_trailing_whitespace("fdjfkld jfjs fjdslfk     "))
print("fdjfkld jfjs fjdslfk" == remove_trailing_whitespace("fdjfkld jfjs fjdslfk     "))
print("fdjfkld jfjs fjdslfk\t")
string = remove_trailing_whitespace('x  \ny   ')

print(string)


# print(repr("x\nw"))