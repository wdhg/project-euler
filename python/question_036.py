convert = lambda x : bin(x)[2:]

def is_palindrome(x):
    x = str(x)
    for i in range(int(len(x) / 2)):
        if x[i] != x[-(i + 1)]:
            return False
    return True

total = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome(convert(i)):
        total += i

print(total)
