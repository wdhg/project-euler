def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

sequence = fib()
total = 0

while True:
    x =  next(sequence)
    if x > 4000000:
        break
    elif x % 2 == 0:
        total += x

print(total)
