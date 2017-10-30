def is_square(x):
    return int(x ** 0.5) == x ** 0.5

layer = 1
total = 0
i = 1

while i <= 1001 ** 2:
    total += i
    if is_square(i):
        layer += 1
    i += 2 * layer - 2

print(total)
