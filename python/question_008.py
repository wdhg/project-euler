with open('question_008_input.txt', 'r') as input_file:
    input_data = input_file.read().replace('\n', '')

def product(x):
    total = 1
    for i in x:
        total *= int(i)
    return total

largest_product = 0

for i in range(len(input_data) - 12):
    local_product = product(input_data[i:i+13])
    if local_product > largest_product:
        largest_product = local_product

print(largest_product)
