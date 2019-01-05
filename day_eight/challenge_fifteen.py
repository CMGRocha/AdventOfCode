from collections import deque

from day_eight import challenge_tree
from utils import file_util

lines = file_util.read_file_return_lines("input.txt")
data = deque()
for line in lines:
    for val in line.split(' '):
        data.append(int(val))

tree = challenge_tree.Tree(data)
print(tree.get_total())
