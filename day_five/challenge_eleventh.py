import sys

from utils import file_util


def size_collision_result(text):
    stack = []
    for letter in text:
        previous_letter = None
        if stack:
            previous_letter = stack[-1]
        if letter != previous_letter and (previous_letter == letter.upper() or previous_letter == letter.lower()):
            stack.pop()
        else:
            stack.append(letter)
    # return stack
    return len(stack)


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    text = ''
    for line in lines:
        text += line.strip()
    unique_letters = set(text.lower())

    polymer = ''
    min_structure = sys.maxsize
    for letter in unique_letters:
        # print(letter)
        text_without_letter = text.replace(letter, '').replace(letter.upper(), '')
        # print(text_without_letter)
        polymer_count = size_collision_result(text_without_letter)
        # print('polymer_count '+str(polymer_count))
        if polymer_count < min_structure:
            min_structure = polymer_count
            polymer = letter
        # return polymer
    return min_structure


print(challenge())
