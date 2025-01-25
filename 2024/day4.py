import numpy as np
'owner'
'proof'
'-4954089-1737782880-78850561a721'


def day4a(xmas_str):
    grid = np.array([list(x.strip()) for x in xmas_str.split()])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_cell(pos, direction, step):
        x = pos[0] + step * direction[0]
        y = pos[1] + step * direction[1]
        if x < 0 or y < 0:
            raise ValueError
        return grid[x, y]

    count = 0
    for pos in zip(*np.where(grid == 'X')):
        for direction in directions:
            try:
                if get_cell(pos, direction, 1) != 'M':
                    continue
                if get_cell(pos, direction, 2) != 'A':
                    continue
                if get_cell(pos, direction, 3) != 'S':
                    continue
            except:
                continue
            count += 1
    return count


def day4b(xmas_str):
    grid = np.array([list(x.strip()) for x in xmas_str.split()])

    def get_cell(pos, direction):
        x = pos[0] + direction[0]
        y = pos[1] + direction[1]
        if x < 0 or y < 0:
            raise ValueError
        return grid[x, y]

    count = 0
    for pos in zip(*np.where(grid == 'A')):
        print(pos)
        try:
            ne = get_cell(pos, (-1, -1))
            se = get_cell(pos, (-1, 1))
            nw = get_cell(pos, (1, -1))
            sw = get_cell(pos, (1, 1))
        except:
            continue
        if (ne != sw) and (se != nw) and ((ne == se and nw == sw) or (ne == nw and se == sw)) and (ne in 'MS') and (sw in "MS"):
            print(True)
            count += 1
    return count


if __name__ == '__main__':
    test_str = """MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX"""
    print(day4b(test_str))
    with open('/home/kan.kawabata/.config/JetBrains/PyCharmCE2023.2/scratches/scratch.txt', 'r') as ifile:
        crossword_str = ifile.read()
        print(day4b(crossword_str))
