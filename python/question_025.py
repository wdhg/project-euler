def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
i = 1
while True:
    num = next(gen)
    if len(str(num)) == 1000:
        print(i)
        exit()
    i += 1
