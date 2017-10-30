def pentagonal(x):
    return int((x * (3 * x - 1)) / 2)

def is_pentagonal(p):
    # Inverse of p=n(n - 1)/3
    return (((24 * p + 1) ** 0.5 + 1) / 6) % 1 == 0

n = 1
while True:
    a = pentagonal(n)
    for i in range(1, n):
        b = pentagonal(i)
        if is_pentagonal(a - b) and is_pentagonal(a + b):
            print(n, i)
            print(a - b)
            exit()
    n += 1
