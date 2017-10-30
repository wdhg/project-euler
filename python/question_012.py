sqrt = lambda x : x ** 0.5

def get_divisor_count(x):
    divisor_count = 0
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            divisor_count += 2
            if i ** 2 == x:
                # Its a square :O
                divisor_count -= 1
    return divisor_count 

number = 0
index = 1

while True:
    if get_divisor_count(number) > 500:
        print(number)
        exit()
    number, index = number + index, index + 1

