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
            if _id not in guards:
                guards[_id] = []
        elif action == "falls asleep":
            start = time
        else:
            guards[_id] += list(range(start, time))

    max_count = 0
    solution = 0
    for guard, minutes in guards.items():
        if minutes:
            most_frequent = Counter(minutes).most_common(1)[0]
            if most_frequent[1] > max_count:
                max_count = most_frequent[1]
                solution = int(guard) * most_frequent[0]
    return solution


print(challenge())
