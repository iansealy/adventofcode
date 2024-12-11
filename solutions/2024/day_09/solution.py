# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from bisect import bisect

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 9

    @answer(6291146824486)
    def part_1(self) -> int:
        # Populate starting lists
        blocks, gaps = self.make_lists()

        # Fill gaps while there are gaps within the files
        while gaps[0][0] < blocks[-1][1]:
            gap_start, gap_end = gaps.pop(0)
            gap_len = gap_end - gap_start + 1
            file_id, block_start, block_end = blocks.pop()
            block_len = block_end - block_start + 1
            if gap_len == block_len:
                # Gap and file are same size, so just add the file where the gap was
                i = bisect(blocks, gap_start, key=lambda x: x[1])
                blocks.insert(i, (file_id, gap_start, gap_end))
            elif gap_len > block_len:
                # Gap is bigger than file, so add the file where the gap was and add
                # back the rest of the gap
                i = bisect(blocks, gap_start, key=lambda x: x[1])
                blocks.insert(i, (file_id, gap_start, gap_start + block_len - 1))
                gaps.insert(0, (gap_start + block_len, gap_end))
            elif gap_len < block_len:
                # File is bigger than gap, so add some of the file where the gap was and
                # add back the rest of the file
                i = bisect(blocks, gap_start, key=lambda x: x[1])
                blocks.insert(i, (file_id, gap_start, gap_end))
                blocks.append(
                    (file_id, block_start, block_start + block_len - gap_len - 1)
                )

        # Calculate checksum
        return sum(
            file_id * sum(range(start, end + 1)) for file_id, start, end in blocks
        )

    @answer(6307279963620)
    def part_2(self) -> int:
        # Populate starting lists
        blocks, gaps = self.make_lists()

        for file_id in reversed(range(blocks[-1][0] + 1)):
            file_idx = 0
            # Find current location of file
            for i, block in enumerate(blocks):
                if block[0] == file_id:
                    file_idx = i
                    break
            block_start, block_end = blocks[file_idx][1], blocks[file_idx][2]
            block_len = block_end - block_start + 1

            # Find suitable gap
            for i, gap in enumerate(gaps):
                gap_start, gap_end = gap
                gap_len = gap_end - gap_start + 1
                if gap_len >= block_len and gap_start < block_start:
                    gap_idx = i
                    break
            else:
                # No suitable gap found
                continue

            # Find gap to remove and merge with any neighbouring gaps
            i = bisect(gaps, block_start, key=lambda x: x[0])
            j = i
            new_gap_start = block_start
            new_gap_end = block_end
            if block_start - gaps[i - 1][1] == 1:
                # Merge new gap with neighbouring previous gap
                i -= 1
                new_gap_start = gaps[i][0]
            if j < len(gaps) and gaps[j][0] - block_end == 1:
                # Merge new gap with neighbouring next gap
                new_gap_end = gaps[j][1]
                j += 1
            gaps[i:j] = [(new_gap_start, new_gap_end)]

            # Move file
            i = bisect(blocks, gap_start, key=lambda x: x[1])
            del blocks[file_idx]
            blocks.insert(i, (file_id, gap_start, gap_start + block_len - 1))

            # Remove or resize filled in gap
            if gap_len == block_len:
                # Remove gap
                del gaps[gap_idx]
            else:
                # Adjust start of gap
                gaps[gap_idx] = (gaps[gap_idx][0] + block_len, gaps[gap_idx][1])

        # Calculate checksum
        return sum(
            file_id * sum(range(start, end + 1)) for file_id, start, end in blocks
        )

    def make_lists(self) -> tuple[list, list]:
        blocks = []
        gaps = []
        file_id = 0
        file_block_count = int(self.input[0])
        blocks.append((file_id, 0, file_block_count - 1))  # 1st file
        next_start = file_block_count
        for i in range(1, len(self.input) // 2 + 1):
            file_id += 1
            gap_block_count = int(self.input[i * 2 - 1])
            if gap_block_count:
                gaps.append((next_start, next_start + gap_block_count - 1))
                next_start += gap_block_count
            file_block_count = int(self.input[i * 2])
            blocks.append((file_id, next_start, next_start + file_block_count - 1))
            next_start += file_block_count
        return blocks, gaps
