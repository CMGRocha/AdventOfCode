from utils import file_util


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    text = ''
    for line in lines:
        text += line.strip()

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


print(challenge())
