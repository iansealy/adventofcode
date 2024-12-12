# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from collections import defaultdict

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 11

    @answer(194482)
    def part_1(self) -> int:
        stones = [int(x) for x in self.input.rstrip().split()]
        for _ in range(25):
            new_stones = []
            for stone in stones:
                if stone == 0:
                    new_stones.append(1)
                else:
                    stone_len = len(str(stone))
                    if stone_len % 2 == 0:
                        new_stones.append(int(str(stone)[: stone_len // 2]))
                        new_stones.append(int(str(stone)[stone_len // 2 :]))
                    else:
                        new_stones.append(stone * 2024)
            stones = new_stones

        return len(stones)

    @answer(232454623677743)
    def part_2(self) -> int:
        stones = defaultdict(int, {int(x): 1 for x in self.input.rstrip().split()})
        for _ in range(75):
            new_stones = defaultdict(int)
            for stone in list(stones):
                if stone == 0:
                    new_stones[1] += +stones[0]
                else:
                    stone_len = len(str(stone))
                    if stone_len % 2 == 0:
                        new_stones[int(str(stone)[: stone_len // 2])] += stones[stone]
                        new_stones[int(str(stone)[stone_len // 2 :])] += stones[stone]
                    else:
                        new_stones[stone * 2024] += stones[stone]
            stones = new_stones
        return sum(stones.values())
