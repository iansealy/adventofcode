# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from copy import deepcopy
from multiprocessing import Pool, cpu_count

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    start_i = 0
    start_j = 0
    i_range = 0
    j_range = 0
    directions = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )

    @answer((4939, 1434))
    def solve(self) -> tuple[int, int]:
        grid1 = deepcopy(self.input)
        self.i_range = len(grid1)
        self.j_range = len(grid1[0])
        cur_dir = 0
        # Find start
        for i in range(self.i_range):
            for j in range(self.j_range):
                if grid1[i][j] == "^":
                    self.start_i = i
                    self.start_j = j
        cur_i = self.start_i
        cur_j = self.start_j
        grid1[cur_i] = grid1[cur_i][:cur_j] + "X" + grid1[cur_i][cur_j + 1 :]
        while True:
            next_i = cur_i + self.directions[cur_dir][0]
            next_j = cur_j + self.directions[cur_dir][1]
            # Check if outside grid
            if (
                next_i < 0
                or next_i >= self.i_range
                or next_j < 0
                or next_j >= self.j_range
            ):
                break
            if grid1[next_i][next_j] == "#":
                # Need to turn instead
                cur_dir = (cur_dir + 1) % 4
            else:
                # Mark location as visited and update current position
                cur_i = next_i
                cur_j = next_j
                grid1[cur_i] = grid1[cur_i][:cur_j] + "X" + grid1[cur_i][cur_j + 1 :]
        # Count visited locations
        visited_count = 0
        for i in range(self.i_range):
            visited_count += grid1[i].count("X")

        # Find all possible obstructions
        obstructions = []
        for obstruct_i in range(self.i_range):
            for obstruct_j in range(self.j_range):
                # No obstruction at start location
                if obstruct_i == self.start_i and obstruct_j == self.start_j:
                    continue
                # Obstructions only at locations visited in first part
                if grid1[obstruct_i][obstruct_j] != "X":
                    continue
                obstructions.append((obstruct_i, obstruct_j))

        # Check all possible obstructions in parallel
        p = Pool(cpu_count())
        loop_count = sum(p.map(self.is_loop, obstructions))

        return visited_count, loop_count

    def is_loop(self, obstruction) -> bool:
        grid = deepcopy(self.input)
        cur_dir = 0
        cur_i = self.start_i  # Row
        cur_j = self.start_j  # Col
        # Mark start with direction
        grid[cur_i] = grid[cur_i][:cur_j] + str(cur_dir) + grid[cur_i][cur_j + 1 :]
        # Mark new obstruction
        obstruct_i, obstruct_j = obstruction
        grid[obstruct_i] = (
            grid[obstruct_i][:obstruct_j] + "#" + grid[obstruct_i][obstruct_j + 1 :]
        )
        while True:
            next_i = cur_i + self.directions[cur_dir][0]
            next_j = cur_j + self.directions[cur_dir][1]
            # Check if outside grid
            if (
                next_i < 0
                or next_i >= self.i_range
                or next_j < 0
                or next_j >= self.j_range
            ):
                return False
            if grid[next_i][next_j] == "#":
                # Need to turn instead
                cur_dir = (cur_dir + 1) % 4
            else:
                # Update current position
                cur_i = next_i
                cur_j = next_j
                # Check if been here before heading in same direction
                if grid[cur_i][cur_j] == str(cur_dir):
                    return True
                # Mark location as visited
                grid[cur_i] = (
                    grid[cur_i][:cur_j] + str(cur_dir) + grid[cur_i][cur_j + 1 :]
                )
