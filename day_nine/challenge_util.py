from collections import deque


def get_sequence(max_value, players):
    sequence = deque()
    scores = [0] * players
    for marble in range(0, max_value + 1):
        if marble % 23 == 0 and marble > 0:
            current_player = marble % players
            sequence.rotate(-7)
            scores[current_player] += marble + sequence.pop()
        else:
            sequence.rotate(2)
            sequence.append(marble)
    return scores
