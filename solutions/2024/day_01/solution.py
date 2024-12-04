# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from collections import Counter

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(2430334)
    def part_1(self) -> int:
        """
        Calculate distance
        """
        left_list, right_list = self.get_lists()
        return sum(abs(l - r) for l, r in zip(left_list, right_list))

    @answer(28786472)
    def part_2(self) -> int:
        """
        Calculate similarity score
        """
        left_list, right_list = self.get_lists()
        l_count = Counter(left_list)
        r_count = Counter(right_list)
        return sum(loc_id * r_count[loc_id] * cnt for loc_id, cnt in l_count.items())

    def get_lists(self) -> tuple[list, list]:
        """
        Split input columns into two sorted lists
        """
        left_list = []
        right_list = []
        for line in self.input:
            left, right = line.rstrip().split(maxsplit=2)
            left_list.append(int(left))
            right_list.append(int(right))
        left_list.sort()
        right_list.sort()
        return left_list, right_list
