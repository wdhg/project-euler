numbers = ''

i = 1
while len(numbers) < 1000000:
    numbers += str(i)
    i += 1

total = 1
for power in range(7):
    total *= int(numbers[int(10 ** power) - 1])

print(total)
