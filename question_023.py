def get_divisors(x):
    divisors = [1]
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x / i))
    return list(set(divisors))

# Get a list of abundant numbers
abundant_nums = []
for i in range(1, 28123):
    if sum(get_divisors(i)) > i:
        abundant_nums.append(i)

total = sum(range(28123))
abundant_sums = []
for a in abundant_nums:
    for b in abundant_nums:
        if a + b < 28123:
            abundant_sums.append(a + b)

print(total - sum(set(abundant_sums)))
