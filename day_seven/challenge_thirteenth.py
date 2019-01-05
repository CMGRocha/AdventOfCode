import re
from collections import defaultdict

from utils import file_util

lines = file_util.read_file_return_lines("input.txt")

pattern = re.compile(r'([A-Z]) ')

pairs = map(pattern.findall, lines)
dependant = defaultdict(set)
allow = defaultdict(set)

for first, second in pairs:
    dependant[second].add(first)
    allow[first].add(second)

availables = sorted(set(allow) - set(dependant), reverse=True)
ordered = ''

while availables:

    next_available = availables.pop()
    ordered += next_available
    for element in allow[next_available]:
        if all(dep in ordered for dep in dependant[element]) and element not in availables:
            availables.append(element)
    availables.sort(reverse=True)

print(ordered)
