def reverse_from_left(text):
    if len(text) in (0, 1):
        return text
    return reverse_from_left(text[1:]) + text[0]

def reverse_from_right(text):
    if len(text) in (0, 1):
        return text
    return text[-1] + reverse_from_right(text[:-1])

print(reverse_from_left("testing"))
print(reverse_from_right("testing"))

print(reverse_from_left("abcd"))
print(reverse_from_left("hello"))
print(reverse_from_left(""))