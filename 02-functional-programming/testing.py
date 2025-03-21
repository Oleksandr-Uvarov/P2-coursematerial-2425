def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return(fibonacci(n-1) + fibonacci(n-2))

# print(fibonacci(100))
     


lst = [x + y for x in range(3) for y in range(3) if x != y]

print(lst)