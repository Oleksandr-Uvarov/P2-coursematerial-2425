import random

count = 0
numbers = []

while True:
    number = random.choice(range(365))
    if number not in numbers:
        print(number)
        numbers.append(number)
        count += 1
    else:
        print(number)
        break

print(count)