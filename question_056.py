largest_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = sum(map(int, list(str(a ** b))))
        largest_sum = max(largest_sum, digital_sum)
print(largest_sum)
