# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    @answer(2567)
    def part_1(self) -> int:
        search_word = "XMAS"
        directions = (
            (1, -1),
            (1, 0),
            (1, 1),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        )
        grid = self.input
        total_found = 0
        # Find all possible start points
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == search_word[0]:
                    # Check in all possible directions
                    for direction in directions:
                        found_word = search_word[0]
                        cur_i = i
                        cur_j = j
                        while search_word.startswith(found_word):
                            # Check if word has been found
                            if len(search_word) == len(found_word):
                                total_found += 1
                                break
                            # Check next letters in direction
                            cur_i += direction[0]
                            cur_j += direction[1]
                            # Add letter if still inside grid
                            if (
                                cur_i >= 0
                                and cur_i < len(grid)
                                and cur_j >= 0
                                and cur_j < len(grid[cur_i])
                            ):
                                found_word += grid[cur_i][cur_j]
                            else:
                                break
        return total_found

    @answer(2029)
    def part_2(self) -> int:
        grid = self.input
        total_found = 0
        # Find all possible start points
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if (
                    grid[i][j] == "A"
                    and (
                        grid[i - 1][j - 1] == "M"
                        and grid[i + 1][j + 1] == "S"
                        or grid[i - 1][j - 1] == "S"
                        and grid[i + 1][j + 1] == "M"
                    )
                    and (
                        grid[i - 1][j + 1] == "M"
                        and grid[i + 1][j - 1] == "S"
                        or grid[i - 1][j + 1] == "S"
                        and grid[i + 1][j - 1] == "M"
                    )
                ):
                    total_found += 1
        return total_found
