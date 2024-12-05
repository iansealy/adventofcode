# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(196826776)
    def part_1(self) -> int:
        matches = re.findall(r"mul\((\d+),(\d+)\)", self.input)
        return sum(int(a) * int(b) for a, b in matches)

    @answer(106780429)
    def part_2(self) -> int:
        memory = re.sub(r"don't\(\).*?do\(\)", "", self.input, flags=re.DOTALL)
        memory = re.sub(r"don't\(\).*", "", memory, flags=re.DOTALL)
        matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
        return sum(int(a) * int(b) for a, b in matches)
