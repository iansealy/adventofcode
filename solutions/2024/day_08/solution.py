# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from collections import defaultdict
from itertools import combinations

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    @answer(240)
    def part_1(self) -> int:
        y_range = len(self.input)
        x_range = len(self.input[0])
        antennas = self.group_antennas(x_range, y_range)

        antinodes = defaultdict(dict)
        for coords in antennas.values():
            for coord1, coord2 in combinations(coords, 2):
                x1, y1 = coord1
                x2, y2 = coord2
                x_diff = x1 - x2
                y_diff = y1 - y2
                x3 = x1 + x_diff
                y3 = y1 + y_diff
                x4 = x2 - x_diff
                y4 = y2 - y_diff
                if x3 >= 0 and x3 < x_range and y3 >= 0 and y3 < y_range:
                    antinodes[x3][y3] = True
                if x4 >= 0 and x4 < x_range and y4 >= 0 and y4 < y_range:
                    antinodes[x4][y4] = True

        return sum(len(antinodes[a]) for a in antinodes)

    @answer(955)
    def part_2(self) -> int:
        y_range = len(self.input)
        x_range = len(self.input[0])
        antennas = self.group_antennas(x_range, y_range)

        antinodes = defaultdict(dict)
        for coords in antennas.values():
            for x, y in coords:
                antinodes[x][y] = True  # Antennas are all antinodes
            for coord1, coord2 in combinations(coords, 2):
                x1, y1 = coord1
                x2, y2 = coord2
                x_diff = x1 - x2
                y_diff = y1 - y2

                x3 = x1
                y3 = y1
                while True:
                    x3 = x3 + x_diff
                    y3 = y3 + y_diff
                    if x3 >= 0 and x3 < x_range and y3 >= 0 and y3 < y_range:
                        antinodes[x3][y3] = True
                    else:
                        break

                x4 = x2
                y4 = y2
                while True:
                    x4 = x4 - x_diff
                    y4 = y4 - y_diff
                    if x4 >= 0 and x4 < x_range and y4 >= 0 and y4 < y_range:
                        antinodes[x4][y4] = True
                    else:
                        break

        return sum(len(antinodes[a]) for a in antinodes)

    def group_antennas(self, x_range, y_range) -> defaultdict[str, list]:
        antennas = defaultdict(list)
        for y in range(y_range):
            for x in range(x_range):
                if self.input[y][x] != ".":
                    antennas[self.input[y][x]].append((x, y))
        return antennas
