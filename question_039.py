p = {}

for a in range(1, 1001):
    for b in range(1, 1001):
        c = (a ** 2 + b ** 2) ** 0.5
        # Check if c isn't an integer
        if c % 1 != 0:
            continue
        total = a + b + c
        if total <= 1000:
            p[total] = p[total] + 1 if total in p.keys() else 1

# Find the perimeter value with the largest value, or 'count'
for i in p.keys():
    # If it has the largest values
    if p[i] == max(p.values()):
        print(i)
        exit()
