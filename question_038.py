def is_pandigital(x):
    return ''.join(sorted(x)) == '123456789'

largest = 0
i = 1
for i in range(1, 10001):
    concatenated = ''
    for n in range(1, 10):
        concatenated += str(i * n)
        if is_pandigital(concatenated) and int(concatenated) > largest:
            largest = int(concatenated)
            break
        if len(concatenated) > 9:
            break

print(largest)
