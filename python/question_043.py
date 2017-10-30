from itertools import permutations

divisor_slices = [
    [2, slice(1, 4)],
    [3, slice(2, 5)],
    [5, slice(3, 6)],
    [7, slice(4, 7)],
    [11, slice(5, 8)],
    [13, slice(6, 9)],
    [17, slice(7, 10)]
]

def has_div_property(x):
    for sub_divisor, sub_slice in divisor_slices:
        if int(num[sub_slice]) % sub_divisor != 0:
            return False
    return True



total = 0
for num in permutations(range(10)):
    num = ''.join(map(str, num))
    if has_div_property(num):
        total += int(num)

print(total)
