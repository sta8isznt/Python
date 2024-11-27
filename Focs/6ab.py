import random as rnd

def fermat_check(n):
    if (n == 2 or n == 3):
        return True
    elif n < 2:
        return False
    for i in range(30):
        a = rnd.randint(2, n-1)
        result = pow(a, n-1, n)
        # print(f"Iteration {i+1}: a = {a}, pow(a, n-1, n) = {result}")
        if result != 1:
            return False
    return True


def miller_rabin(n, k=30):
    """
    Perform the Miller-Rabin primality test on n.
    
    Parameters:
    n : int
        The number to test for primality.
    k : int
        The number of rounds to test for primality. More rounds reduce the probability of error.
    
    Returns:
    bool
        True if n is probably prime, False if n is composite.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform the test k times
    for _ in range(k):
        # Choose a random base a
        a = rnd.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)  # Compute x^2 % n
            if x == n - 1:
                break
        else:
            return False

    return True


num = int("58.094.662.081".replace('.', ''))  
print(num)        
print(fermat_check(num))
print(miller_rabin(num))