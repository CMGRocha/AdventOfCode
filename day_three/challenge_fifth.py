# challenge_fifth.py
from utils import file_util


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    # lines = file_util.read_file_return_lines("test.txt")
    # .strip()
    # split(', ')
    result = 0
    area = dict()
    for line in lines:
        line = line.strip()
        useful_part = line.split('@')[1]

        location = useful_part.split(':')[0].strip()
        size = useful_part.split(':')[1].strip()

        location_y = location.split(',')[0].strip()
        location_x = location.split(',')[1].strip()

        size_y = size.split('x')[0].strip()
        size_x = size.split('x')[1].strip()

        for x in range(int(location_x), int(location_x) + int(size_x)):
            for y in range(int(location_y), int(location_y) + int(size_y)):
                pos = "" + str(x) + "," + str(y)
                area[pos] = area.get(pos, 0) + 1

        # print(area)

    for value in area.values():
        if value > 1:
            result += 1

    print(result)


challenge()
