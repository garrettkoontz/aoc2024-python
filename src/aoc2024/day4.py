from src.aoc2024.util import read_file


def part1():
    ws = read_file("../inputs/day4.txt").split("\n")
    search_string = "XMAS"
    __stop = len(search_string)
    count = 0
    pts = []
    for y in range(0, len(ws)):
        for x in range(0, len(ws[0])):
            diags = search_diagonals(x, y, __stop, ws, search_string)
            pts += diags if len(diags) > 0 else []
            count += len(list(diags.values())[0]) if len(list(diags.values())) > 0 else 0
    print(pts)
    return count


def diagonals(x, y, __stop, ws):
    ps = []
    if x + __stop <= len(ws[0]):
        ps.append([(x + i, y) for i in range(0, __stop)])
    if x - __stop >= -1:
        ps.append([(x - i, y) for i in range(0, __stop)])
    if y + __stop <= len(ws):
        ps.append([(x, y + i) for i in range(0, __stop)])
    if y - __stop >= -1:
        ps.append([(x, y - i) for i in range(0, __stop)])
    if x + __stop <= len(ws[0]) and y + __stop <= len(ws):
        ps.append([(x + i, y + i) for i in range(0, __stop)])
    if x - __stop >= -1 and y - __stop >= -1:
        ps.append([(x - i, y - i) for i in range(0, __stop)])
    if y + __stop <= len(ws) and x - __stop >= -1:
        ps.append([(x - i, y + i) for i in range(0, __stop)])
    if y - __stop >= -1 and x + __stop <= len(ws[0]):
        ps.append([(x + i, y - i) for i in range(0, __stop)])
    return ps


def search_diagonals(x, y, __stop, ws, search_string):
    xmas = {}
    for pts in diagonals(x, y, __stop, ws):
        if search_string == ''.join([ws[j][k] for (j, k) in pts]):
            p = xmas.get((x, y), [])
            p.append(dict.fromkeys(pts))
            xmas[(x, y)] = p
    return xmas


def part2():
    ws = read_file("../inputs/day4.txt").split("\n")
    count = 0
    ms = {"M", "S"}
    for y in range(1, len(ws) - 1):
        for x in range(1, len(ws[0]) - 1):
            w = ws[y][x]
            dur = ws[y + 1][x + 1]
            dul = ws[y - 1][x + 1]
            ddr = ws[y + 1][x - 1]
            ddl = ws[y - 1][x - 1]
            if w == "A" and dur != ddl and dul != ddr and {dur, dul, ddr, ddl} == ms:
                count += 1
    return count


def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
