def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

primes = [2]
i = 1
while True:
    i += 2
    if is_prime(i):
        primes.append(i)
    else:
        works = False
        for prime in primes:
            if (((i - prime) / 2) ** 0.5) % 1 == 0:
                works = True
        if not works:
            print(i)
            exit()
