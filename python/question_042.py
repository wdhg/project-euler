from string import ascii_uppercase as letters

with open('question_042_input.txt', 'r') as input_file:
    input_data = input_file.read().replace('"', '').split(',')

def convert_word(word):
    total = 0
    for letter in word:
        total += letters.index(letter) + 1
    return total

# Find max possible value by multiplying the length of the longest word by 26
max_value = 0
for word in input_data:
    max_value = max(max_value, len(word) * len(letters))

# Generate a list of triangle numbers
triangle_numbers = [1]
n = 2
while triangle_numbers[-1] <= max_value:
    triangle_numbers.append(0.5 * n * (n + 1))
    n += 1

count = 0
for word in input_data:
    if convert_word(word) in triangle_numbers:
        count += 1

print(count)
