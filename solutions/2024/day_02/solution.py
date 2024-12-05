# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(606)
    def part_1(self) -> int:
        safe_count = 0
        for line in self.input:
            report = [int(level) for level in line.rstrip().split()]
            if self.check_report_safe(report):
                safe_count += 1

        return safe_count

    @answer(644)
    def part_2(self) -> int:
        safe_count = 0
        for line in self.input:
            report = [int(level) for level in line.rstrip().split()]
            if self.check_report_safe(report):
                safe_count += 1
                continue

            # Try removing each level
            for idx in range(len(report)):
                if self.check_report_safe(report[:idx] + report[idx + 1 :]):
                    safe_count += 1
                    break

        return safe_count

    def check_report_safe(self, report) -> bool:
        """
        Check if report is safe
        """
        diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
        # Check if not increasing or decreasing, or increasing or decreasing too much
        if any(d == 0 or d > 3 or d < -3 for d in diffs):
            return False
        # Check if mix of increasing and decreasing
        if any(d < 0 for d in diffs) and any(d > 0 for d in diffs):  # noqa: SIM103
            return False
        return True
