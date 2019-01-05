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
done = []

workers = [{'remain': 0, 'task': None} for _ in range(5)]

t = -1
while availables or any(w['task'] is not None for w in workers):
    t += 1
    for worker in workers:
        if worker['task'] is not None and worker['remain'] == 0:
            task = worker['task']
            done.append(task)
            worker['task'] = None
            for element in allow[task]:
                if all(dep in done for dep in dependant[element]) and element not in availables:
                    availables.append(element)
            availables.sort(reverse=True)

        if worker['remain'] == 0 and availables and worker['task'] is None:
            next_available = availables.pop()
            req_time = ord(next_available) - 4
            worker['remain'] = req_time
            worker['task'] = next_available

        worker['remain'] = max(0, worker['remain'] - 1)

print(t)
