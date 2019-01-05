import re

from day_nine import challenge_util
from utils import file_util

lines = file_util.read_file_return_lines("input.txt")
for line in lines:
    players, last_marble = [int(n) for n in re.findall(r'\d+', line)]
    large_scores = challenge_util.get_sequence(last_marble * 100, players)
    print(max(large_scores))
