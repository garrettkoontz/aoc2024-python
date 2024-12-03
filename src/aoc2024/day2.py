from src.aoc2024.util import read_file


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
def is_safe(l: list[int]) -> int:
    if l[0] - l[1] == 0:
        return 0
    dir = 1 if l[0] - l[1] < 0 else -1
    for i in range(0, len(l) - 1):
        d = l[i] - l[i + 1]
        if (1 if d < 0 else -1) != dir:
            return i
        if d == 0 or d > 3 or d < -3:
            return i
    return -1


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# Remove first problem level
def is_dampener_safe(l: list[int]) -> bool:
    i = is_safe(l)
    if i == -1: return True
    (a,b,c) = (is_safe(l[:i-1] + l[i :]),
               is_safe(l[:i] + l[i+1 :]),
               is_safe(l[:i+1] + l[i + 2 :]))
    if a == -1 or b == -1 or c == -1: return True
    return False



def part1():
    d = read_file("../inputs/day2.txt").split("\n")
#     d = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".split("\n")
    levels = [[int(y) for y in x.split(" ")] for x in d]
    o = 0
    for l in levels:
        o += 1 if is_safe(l) == -1 else 0
    return o


def part2():
    d = read_file("../inputs/day2.txt").split("\n")
#     d = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9""".split("\n")
    levels = [[int(y) for y in x.split(" ")] for x in d]
    o = 0
    for l in levels:
        o += 1 if is_dampener_safe(l) else 0
    return o
# 604 too low, but probably close
# 608 too low

def __init__():
    print(part1())
    print(part2())


__init__()
