import math

def product(x):
    total = 1
    for i in x:
        total *= i
    return total

def get_smallest_factor(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x

def get_prime_factors(x):
    prime_factors = [
        get_smallest_factor(x)
    ]
    temp_factor = x / prime_factors[-1]
    while product(prime_factors) < x:
        prime_factors.append(get_smallest_factor(temp_factor))
        temp_factor = int(temp_factor / prime_factors[-1])
    return prime_factors

# Lowest common multiple
def get_lcm(a, b):
    a_primes = get_prime_factors(a)
    b_primes = get_prime_factors(b)
    lcm = 1
    for i in set(a_primes + b_primes):
        lcm *= i ** max(a_primes.count(i), b_primes.count(i))
    return lcm

last_lcm = 1
for i in range(1, 21):
    last_lcm = get_lcm(last_lcm, i)
print(last_lcm)
