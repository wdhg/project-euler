def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_circular_prime(x):
    x_str = str(x)
    for i in range(len(x_str)):
        if not is_prime(int(x_str[i:] + x_str[:i])):
            return False
    return True

count = 0
for i in range(1000000):
    if is_circular_prime(i):
        count += 1

print(count)
