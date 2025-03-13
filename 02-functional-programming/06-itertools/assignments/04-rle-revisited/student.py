from itertools import groupby

# def rle_encode(data):
#     data = iter(data)
#     count = 1
#     try: 
#         previous_char = next(data)
#     except StopIteration:
#         # yield data 
#         return data
    
#     for char in data:
#         if previous_char != char:
#             yield(previous_char, count)
#             previous_char = char
#             count = 0
#         count += 1
        
#     yield(previous_char, count)

def rle_encode(data):
    test = groupby(data)
    yield ((e[0], len(list(e[1]))) for e in test)

def rle_decode(data):
    for pair in data:
        for i in range(pair[1]):
            yield pair[0] 




# print(groupby(["abcedefweg", len]))
# print(groupby(['a', 'a', 'bdef'], len))

soe = groupby(['a', 'a', 'b', 'bdef'], len)

# test = groupby("aaaaffewefefwgewkotr")
test = iter("aneugnwgiwegmgeo")
for char, group in groupby(test):
    print(char, list(group))

test2 = groupby(iter("fewegwge"))

for e in test2:
    print(e[0], list(e[1]))

data = iter("aaabbcccc")  # Now an iterator
for char, group in groupby(data):
    print(char, list(group))  # list() consumes the iterator


# for e in test:
#     print(e[0], list(e[1]))
# soe = groupby(["abcedefweg"], len)

# for s in soe:
#     print(s[0], list(s[1]))






# # def rle_encode(data):
# #     return ((char, 1) for char in data)


# data = "a"
# data = "aa"
# data = "aaa"
# data = "aaab"
# data = "aaaabcccc"
# data = [('a', 1)]

# # data = "xyz"

# encode = rle_encode(data)
# for e in encode:
#     print(e)