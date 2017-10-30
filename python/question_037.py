def is_prime(x):
    x = int(x)
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(x):
    x = str(x)
    for i in range(len(x)):
        if not is_prime(x[i::]) or not is_prime(x[:(i + 1)]):
            return False
    return True

total = 0
count = 0
num = 11
while count < 11:
    if is_truncatable_prime(num):
        count += 1
        total += num
    num += 1

print(total)
