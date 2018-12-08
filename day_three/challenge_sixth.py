# challenge_fifth.py
from utils import file_util


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    # lines = file_util.read_file_return_lines("test.txt")
    # .strip()
    # split(', ')
    all_owners = set()
    conflict_owners = set()
    area = dict()
    owner_map = dict()
    for line in lines:
        line = line.strip()
        id_claim = line.split('@')[0].strip()
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
                all_owners.add(id_claim)

                if area[pos] > 1:
                    conflict_owners.add(str(id_claim))
                    conflict_owners.add(str(owner_map[pos]))

                owner_map[pos] = str(id_claim)
        # print(area)

    print(all_owners.difference(conflict_owners))


challenge()
