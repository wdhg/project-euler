import math

def get_smallest_factor(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return i
    return x

def product(x):
    total = 1
    for i in x:
        total *= i
    return total

def get_prime_factors(x):
    prime_factors = [
        get_smallest_factor(x)
    ]
    temp_factor = x / prime_factors[-1]
    while product(prime_factors) < x:
        prime_factors.append(get_smallest_factor(temp_factor))
        temp_factor = temp_factor / prime_factors[-1]

    return prime_factors

print(get_prime_factors(13195))
print(max(get_prime_factors(600851475143)))
