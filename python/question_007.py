sqrt = lambda x : x ** 0.5 

def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime_count = 0
number = 1
while prime_count < 10001:
    number += 1
    if is_prime(number):
        prime_count += 1

print(number)
