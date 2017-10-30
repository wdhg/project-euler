def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def get_recurring_len(x):
    # Basically just bus stop / short hand division to get the length
    length = 0
    carried = [10]
    while True:
        length += 1
        carry = (carried[-1] % x) * 10
        if carry in carried:
            break
        else:
            carried.append(carry)
    return length

longest_len = 0
longest = 0
for i in range(1, 1000):
    if is_prime(i):
        recurring_len = get_recurring_len(i)
        if recurring_len > longest_len:
            longest_len = recurring_len
            longest = i

print(longest)
