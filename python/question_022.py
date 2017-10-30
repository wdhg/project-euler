from string import ascii_uppercase as letters

with open('question_022_input.txt', 'r') as input_file:
    input_data = sorted(input_file.read().replace('"', '').split(','))

total = 0
for index in range(len(input_data)):
    for letter in input_data[index]:
        total += (index + 1) * (letters.index(letter) + 1)

print(total)
