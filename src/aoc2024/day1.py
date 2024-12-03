import math

from src.aoc2024.util import read_file


def part1():
    f = read_file("../inputs/day1.txt")
    fs = f.split("\n")
    a = []
    b = []
    for l in fs:
        c = l.split("   ")
        a.append(int(c[0]))
        b.append(int(c[1]))
    a.sort()
    b.sort()
    return sum([math.fabs(a[i] - b[i]) for i in range(0, len(a))])

def part2():
    f = read_file("../inputs/day1.txt")
    fs = f.split("\n")
    a = []
    b = []
    for l in fs:
        c = l.split("   ")
        a.append(int(c[0]))
        b.append(int(c[1]))
    a.sort()
    b.sort()
    d = {}
    for i in b:                   
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return sum([j * d[j] for j in a if j in d])

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()