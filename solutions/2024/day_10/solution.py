# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10

    i_range = 0
    j_range = 0
    directions = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )

    @answer((709, 1326))
    def solve(self) -> tuple[int, int]:
        self.i_range = len(self.input)
        self.j_range = len(self.input[0])

        # Find trailheads
        total_score = 0
        total_rating = 0
        for i in range(self.i_range):
            for j in range(self.j_range):
                if self.input[i][j] == "0":
                    nines_set, nines_list = self.climb_trail(i, j, 0)
                    total_score += len(nines_set)
                    total_rating += len(nines_list)

        return total_score, total_rating

    def climb_trail(self, i, j, height) -> tuple[set, list]:
        # Base case
        if self.input[i][j] == "9":
            return {(i, j)}, [(i, j)]

        # Look for next step in trail in each direction
        nines_set = set()
        nines_list = []
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            next_h = height + 1
            if (
                next_i >= 0
                and next_i < self.i_range
                and next_j >= 0
                and next_j < self.j_range
                and self.input[next_i][next_j] == str(next_h)
            ):
                new_nines_set, new_nines_list = self.climb_trail(next_i, next_j, next_h)
                nines_set = nines_set.union(new_nines_set)
                nines_list.extend(new_nines_list)

        return nines_set, nines_list
