# def rle_encode(data):
#     count = 0
#     previous_char = None
#     if type(data) in (dict, list, tuple, str):
#         if len(data) == 0:
#             return data
#         previous_char = data[0]
#     else:
#         count = 1
#         try: 
#             previous_char = next(data)
#         except StopIteration:
#             # yield data 
#             return data
    
#     for char in data:
#         if previous_char != char:
#             yield(previous_char, count)
#             previous_char = char
#             count = 0
#         count += 1
        
#     yield(previous_char, count)

def rle_encode(data):
    data = iter(data)
    count = 1
    try: 
        previous_char = next(data)
    except StopIteration:
        # yield data 
        return data
    
    for char in data:
        if previous_char != char:
            yield(previous_char, count)
            previous_char = char
            count = 0
        count += 1
        
    yield(previous_char, count)

# def rle_encode(data):
#     return ((char, 1) for char in data)


data = "a"
data = "aa"
data = "aaa"
data = "aaab"
data = "aaaabcccc"
data = [('a', 1)]

# data = "xyz"

encode = rle_encode(data)
for e in encode:
    print(e)


def rle_decode(data):
    for pair in data:
        for i in range(pair[1]):
            yield pair[0] 




# # string = "aaabccc"
# string = "abababab"
# # string = "a"

# encode = rle_encode(string)

# decode = rle_decode(encode)
# for ch in decode:
#     print(ch)





