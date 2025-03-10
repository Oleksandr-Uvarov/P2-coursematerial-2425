def fun(max):
    cnt = 1

    while cnt <= max:
        yield cnt
        cnt += 1


numbers = fun(5)
for number in numbers:
    print(number)