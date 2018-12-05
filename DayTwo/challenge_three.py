# challenge_three.py

from utils import file_util

lines = file_util.read_file_return_lines("input.txt")
# lines = file_util.read_file_return_lines("test.txt")

repetition_of_two = 0
repetition_of_three = 0

for line in lines:
    dictionary = dict()
    for letter in line:
        dictionary[letter] = dictionary.get(letter, 0) + 1

    if 2 in dictionary.values():
        repetition_of_two += 1

    if 3 in dictionary.values():
        repetition_of_three += 1

print(repetition_of_two * repetition_of_three)


