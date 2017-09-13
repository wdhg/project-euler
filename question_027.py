def is_prime(x):
    x = abs(x)
    if x == 0 or x == 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

highest_n = 0
best_a = 0
best_b = 0
for a in range(-1000, 1000):
    print(a, end='\r')
    for b in range(-1001, 1001):
        n = 0
        while is_prime((n ** 2) + (a * n) + b):
            n += 1
        if n > highest_n:
            highest_n = n
            best_a = a
            best_b = b

print(highest_n)
print(best_a * best_b)
