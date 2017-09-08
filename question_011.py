with open('question_011_input.txt', 'r') as input_file:
    input_data = list(map(
        lambda x : list(map(int, x.split())),
        input_file.read().split('\n')
    ))[0:-1] # Slice is to get rid of an empty list on the end

def product(x):
    total = 1
    for i in x:
        total *= i
    return total

greatest_product = 0

# Check horizonal
for y in range(len(input_data)):
    for x in range(len(input_data[y]) - 3):
        greatest_product = max(
            greatest_product,
            product(input_data[y][x:x+4])
        )

# Check vertical and diagonal
for y in range(len(input_data) - 3):
    for x in range(len(input_data[y])):
        # Vertical
        greatest_product = max(
            greatest_product,
            product([input_data[y + i][x] for i in range(4)])
        )
        # Diagonal left to right
        if x < len(input_data[y]) - 3:
            greatest_product = max(
                greatest_product,
                product([input_data[y + i][x + i] for i in range(4)]),
                product([input_data[y + i][-x - i] for i in range(4)])
            )

print(greatest_product)
