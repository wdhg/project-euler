sqrt = lambda x : x ** 0.5

def is_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

total = 0
for i in range(2, 2000001):
    if is_prime(i):
        total += i
print(total)
