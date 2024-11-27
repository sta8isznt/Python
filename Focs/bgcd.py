def bgcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    # Και οι δύο άρτιοι
    if a % 2 == 0 and b % 2 == 0:
        return 2 * bgcd(a // 2, b // 2)
    # Μόνο το a άρτιο
    elif a % 2 == 0:
        return bgcd(a // 2, b)
    # Μόνο το b άρτιο
    elif b % 2 == 0:
        return bgcd(a, b // 2)
    # Και οι δύο περιττοί
    else:
        return bgcd(min(a, b), abs(a - b) // 2)

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a


import random
import time

# Δημιουργία 100 ζευγών μεγάλων αριθμών
test_cases = [(random.randint(10**10, 10**12), random.randint(10**10, 10**12)) for _ in range(10)]

# Μέτρηση χρόνου για Binary GCD
start_time = time.time()
for a, b in test_cases:
    bgcd(a, b)
binary_gcd_time = time.time() - start_time

# Μέτρηση χρόνου για Ευκλείδειο αλγόριθμο
start_time = time.time()
for a, b in test_cases:
    gcd_euclidean(a, b)
euclidean_gcd_time = time.time() - start_time

print(f"Binary GCD time: {binary_gcd_time:.200f} seconds")
print(f"Euclidean GCD time: {euclidean_gcd_time:.200f} seconds")
