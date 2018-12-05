# challenge_four.py
from collections import Counter

from utils import file_util


def num_common_letters(string_a, string_b):
    a_counter = Counter(string_a)
    b_counter = Counter(string_b)
    return sum(min(a_counter[key], b_counter[key]) for key in a_counter)


# bad english
def is_one_letter_different(string1, string2):
    difference = 0
    for x, y in zip(string1, string2):
        if x != y:
            difference += 1
    return difference == 1


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    # lines = file_util.read_file_return_lines("test_2.txt")

    my_list = []
    for line in lines:
        for temp_line in lines:
            if is_one_letter_different(line, temp_line):
                my_list.append(line)
                my_list.append(temp_line)
                break
        if my_list:
            break

    answer = ""
    for letter in my_list[0]:
        if letter in my_list[1]:
            answer += letter

    return answer


print(challenge())
# print(tuple(zip('ola', 'ola')))
# not the answer qwugbihrkclyvpjaxefotvdzns
