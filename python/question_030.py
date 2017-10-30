i = 2
total = 0
while i < 1000000:
    power_sums = 0
    for num in str(i):
        power_sums += int(num) ** 5
    if power_sums == i:
        total += i
    i += 1

print(total)
