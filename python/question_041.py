from itertools import permutations

def is_prime(x):
    if x <= 1 or x % 2 == 0:
        return False
    if x <= 3:
        return True
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

# Starting from 7 because the sums of the numbers 1 to 9 and 1 to 8 are
# divisible by 3, so therefore no pandigital number with these numbers can
# be prime
for i in range(7, 0, -1):
    for n in permutations(range(i, 0, -1)):
        n = int(''.join(map(str, n)))
        if is_prime(n):
            print(n)
            exit()
