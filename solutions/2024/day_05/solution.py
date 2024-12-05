# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from collections import defaultdict
from copy import deepcopy

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    @answer(4185)
    def part_1(self) -> int:
        rules, updates = self.get_input()
        middle_total = 0
        for update in updates:
            incorrect_order = False
            for i in range(len(update) - 1):
                for j in range(i + 1, len(update)):
                    if update[i] in rules and update[j] in rules[update[i]]:
                        incorrect_order = True
                        break
                if incorrect_order:
                    break
            if not incorrect_order:
                middle_total += int(update[(len(update) - 1) // 2])

        return middle_total

    @answer(4480)
    def part_2(self) -> int:
        rules, updates = self.get_input()
        middle_total = 0
        for update in updates:
            # Ignore updates with correct order
            incorrect_order = False
            for i in range(len(update) - 1):
                for j in range(i + 1, len(update)):
                    if update[i] in rules and update[j] in rules[update[i]]:
                        incorrect_order = True
                        break
                if incorrect_order:
                    break
            if not incorrect_order:
                continue

            # Reduce graph to just pages in update
            graph = deepcopy(rules)
            for page1 in list(graph.keys()):
                if page1 not in update:
                    del graph[page1]
                else:
                    for page2 in list(graph[page1]):
                        if page2 not in update:
                            del graph[page1][page2]

            # Depth first search
            visited = set()
            order = []
            for page in list(graph.keys()):
                if page not in visited:
                    visited, order = self.dfs(graph, page, visited, order)
            middle_total += int(order[(len(order) - 1) // 2])

        return middle_total

    def get_input(self) -> tuple[defaultdict, list]:
        rules = defaultdict(dict)
        updates = []
        for line in self.input:
            if "|" in line:
                p1, p2 = line.rstrip().split("|", maxsplit=2)
                rules[p1][p2] = True
            elif "," in line:
                updates.append(line.rstrip().split(",")[::-1])
        return rules, updates

    def dfs(self, graph, node, visited, order) -> tuple[set, list]:
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited, order = self.dfs(graph, neighbour, visited, order)
        order.append(node)
        return visited, order
