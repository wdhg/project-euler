with open('question_013_input.txt', 'r') as input_file:
    input_data = list(map(int, input_file.read().split()))

print(str(sum(input_data))[0:10])
