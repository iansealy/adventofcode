# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    @answer(2941973819040)
    def part_1(self) -> int:
        total_calibration = 0
        for line in self.input:
            test_value, nums = line.rstrip().split(":", maxsplit=2)
            test_value = int(test_value)
            nums = [int(n) for n in nums.split()]
            values = [nums.pop(0)]
            for num in nums:
                new_values = []
                for value in values:
                    new_value = value + num
                    if new_value <= test_value:
                        new_values.append(new_value)
                    new_value = value * num
                    if new_value <= test_value:
                        new_values.append(new_value)
                values = new_values
            if test_value in values:
                total_calibration += test_value
        return total_calibration

    # @answer(1234)
    def part_2(self) -> int:
        total_calibration = 0
        for line in self.input:
            test_value, nums = line.rstrip().split(":", maxsplit=2)
            test_value = int(test_value)
            nums = [int(n) for n in nums.split()]
            values = [nums.pop(0)]
            for num in nums:
                new_values = []
                for value in values:
                    new_value = value + num
                    if new_value <= test_value:
                        new_values.append(new_value)
                    new_value = value * num
                    if new_value <= test_value:
                        new_values.append(new_value)
                    new_value = int(str(value) + str(num))
                    if new_value <= test_value:
                        new_values.append(new_value)
                values = new_values
            if test_value in values:
                total_calibration += test_value
        return total_calibration
