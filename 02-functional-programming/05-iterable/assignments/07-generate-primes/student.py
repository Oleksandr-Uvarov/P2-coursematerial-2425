def is_prime(n):
    if n in [0, 1]:
        return False
    
    return all(False if n % i == 0 else True for i in range(2, n))

def primes():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1