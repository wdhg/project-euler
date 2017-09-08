total_a = 0
total_b = 0

for i in range(101):
    total_a += i ** 2
    total_b += i

print((total_b ** 2) - total_a)
