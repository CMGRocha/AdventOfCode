import re
from collections import Counter

from utils import file_util


def challenge():
    lines = file_util.read_file_return_lines("input.txt")
    data = []
    for line in lines:
        date = line[line.find("[") + 1:line.find("]")]
        action = line.split("] ")[1].strip()
        data.append((date, action,))
    data = sorted(data, key=lambda i: i[0])

    guards = {}
    for time, action in data:
        time = int(time[-2:])
        if "Guard" in action:
            _id = re.findall(r'\d+', action)[0]
            if not _id in guards:
                guards[_id] = {'length': 0, 'minutes': []}
        elif action == "falls asleep":
            start = time
        else:
            guards[_id]['length'] += time - start
            guards[_id]['minutes'] += list(range(start, time))

    sleep_longest = max(guards.items(), key=lambda guard: guard[1]['length'])
    minutes = sleep_longest[1]['minutes']
    return Counter(minutes).most_common(1)[0][0] * int(sleep_longest[0])


print(challenge())
