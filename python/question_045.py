def is_triangle(x):
    return (((8 * x + 1) ** 0.5 + 1) / 2) % 1 == 0

def is_pentagonal(x):
    return (((24 * x + 1) ** 0.5 + 1) / 6) % 1 == 0

i = 0
count = 0
while count < 3:
    i += 1
    h = i * (2 * i - 1)
    if is_triangle(h) and is_pentagonal(h):
        print(h)
        count += 1
