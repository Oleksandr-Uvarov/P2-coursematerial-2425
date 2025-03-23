def summing_up_number(n):
    if n == 1:
        return 1
    
    return n + (summing_up_number(n - 1))

# 5 + 4 + 3 + 2 + 1 
print(summing_up_number(5))




# 5!
# 1 * 2 * 3 * 4 * 5
# 5 * 4 * 3 * 2 * 1 

def factorial_recursive(n):
    if n == 1: 
        return 1
    
    return n * factorial_recursive(n - 1)
    # 5 * factorial_recursive(4)
    # 4 * factorial_recursive(3)
    # 3 * factorial_recursive(2)
    # 2 * factorial_recursive(1)
    # 1

    # 5 * 4 * 3 * 2 * 1

# print(factorial_recursive(5))

# [1,2,3,4]


# [3, 4]
