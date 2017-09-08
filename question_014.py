def get_collatz_len(x):
    length = 0

    while x > 1:
        if x % 2 == 0:
            x /= 2
            length += 1
        else:
            x = (3 * x + 1) / 2 
            length += 2
    return length

longest = 0
longest_len = 0

for i in range(1000000):
    chain_len = get_collatz_len(i)
    if chain_len > longest_len:
        longest = i
        longest_len = chain_len

print(longest)
