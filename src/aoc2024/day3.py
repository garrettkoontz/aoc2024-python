import re

from src.aoc2024.util import read_file

def part1():
    regex = r'mul\((\d+),(\d+)\)'
    d = read_file("../inputs/day3.txt")
    muls = re.findall(regex, d)
    r = 0
    for m in muls:
        r += int(m[0]) * int(m[1])
    return r


def part2():
    regex = r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))'
    d = read_file("../inputs/day3.txt")
    muls = re.findall(regex, d)
    print(muls)
    r = 0
    do = True
    for m in muls:
        if m[0] == "":
            if m[2] == "do()":
                do = True
            else:
                do = False
            continue
        if do:
            r += int(m[0]) * int(m[1])
    return r

def __init__():
    print(part1())
    print(part2())


__init__()
