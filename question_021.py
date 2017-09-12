def get_divisors(x):
    divisors = [1]
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(int(x / i))
    return list(set(divisors))

amicable = []
for num in range(1, 10001):
    divisor_sum = sum(get_divisors(num))
    if sum(get_divisors(divisor_sum)) == num and num != divisor_sum:
        if num not in amicable:
            amicable.append(num)
        if divisor_sum not in amicable:
            amicable.append(divisor_sum)

print(sum(amicable))
