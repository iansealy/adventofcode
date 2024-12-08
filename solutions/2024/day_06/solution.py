# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from copy import deepcopy

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    @answer((4939, 1434))
    def solve(self) -> tuple[int, int]:
        grid1 = deepcopy(self.input)
        i_range = len(grid1)
        j_range = len(grid1[0])
        directions = (
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1),
        )
        cur_dir = 0
        start_i = 0  # Row
        start_j = 0  # Col
        # Find start
        for i in range(i_range):
            for j in range(j_range):
                if grid1[i][j] == "^":
                    start_i = i
                    start_j = j
        cur_i = start_i
        cur_j = start_j
        grid1[cur_i] = grid1[cur_i][:cur_j] + "X" + grid1[cur_i][cur_j + 1 :]
        while True:
            next_i = cur_i + directions[cur_dir][0]
            next_j = cur_j + directions[cur_dir][1]
            # Check if outside grid
            if next_i < 0 or next_i >= i_range or next_j < 0 or next_j >= j_range:
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
        for i in range(i_range):
            visited_count += grid1[i].count("X")

        loop_count = 0
        for obstruct_i in range(i_range):
            for obstruct_j in range(j_range):
                # No obstruction at start location
                if obstruct_i == start_i and obstruct_j == start_j:
                    continue
                # Obstructions only at locations visited in first part
                if grid1[obstruct_i][obstruct_j] != "X":
                    continue
                grid2 = deepcopy(self.input)
                cur_dir = 0
                cur_i = start_i  # Row
                cur_j = start_j  # Col
                # Mark start with direction
                grid2[cur_i] = (
                    grid2[cur_i][:cur_j] + str(cur_dir) + grid2[cur_i][cur_j + 1 :]
                )
                # Mark new obstruction
                grid2[obstruct_i] = (
                    grid2[obstruct_i][:obstruct_j]
                    + "#"
                    + grid2[obstruct_i][obstruct_j + 1 :]
                )
                while True:
                    next_i = cur_i + directions[cur_dir][0]
                    next_j = cur_j + directions[cur_dir][1]
                    # Check if outside grid
                    if (
                        next_i < 0
                        or next_i >= i_range
                        or next_j < 0
                        or next_j >= j_range
                    ):
                        break
                    if grid2[next_i][next_j] == "#":
                        # Need to turn instead
                        cur_dir = (cur_dir + 1) % 4
                    else:
                        # Update current position
                        cur_i = next_i
                        cur_j = next_j
                        # Check if been here before heading in same direction
                        if grid2[cur_i][cur_j] == str(cur_dir):
                            loop_count += 1
                            break
                        # Mark location as visited
                        grid2[cur_i] = (
                            grid2[cur_i][:cur_j]
                            + str(cur_dir)
                            + grid2[cur_i][cur_j + 1 :]
                        )

        return visited_count, loop_count
