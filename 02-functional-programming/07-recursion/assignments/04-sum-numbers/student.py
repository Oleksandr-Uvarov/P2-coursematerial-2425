def sum_numbers(number):
    if number < 0:
        number = -number

    if len(str(number)) == 1:
        return number
    
    first_digit = int(str(number)[0])

    rest_of_number = int(str(number)[1:])
    
    return first_digit + sum_numbers(rest_of_number)

print(sum_numbers(234))
print(sum_numbers(-234))
print(sum_numbers(123456789))

print(234 % 10)