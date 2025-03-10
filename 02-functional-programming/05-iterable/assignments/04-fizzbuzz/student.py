# def fizzbuzz():
#     number = 1
#     while True:
#         if number % 3 == 0 and number % 5 == 0:
#             yield "fizzbuzz"
#         elif number % 3 == 0:
#             yield "fizz"
#         elif number % 5 == 0:
#             yield "buzz"
#         else:
#             yield str(number)
#         number += 1

def fizzbuzz():
    number = 1
    while True:
        result = ""
        if number % 3 == 0:
            result += "fizz"
        if number % 5 == 0:
            result += "buzz"
        
        if result != "":
            yield result
        else:
            yield str(number)
        number += 1


# numbers = fizzbuzz(30)

# for number in numbers:
#     print(number)