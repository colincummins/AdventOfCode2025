# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer
from collections import defaultdict


class Solution(StrSplitSolution):
    _year = 2025
    _day = 5

    def preprocess(self) -> None:
        splitIndex = self.input.index("")
        self.idRanges, self.ingredients = self.input[0:splitIndex], self.input[splitIndex + 1:]
        self.idRanges = [list(map(int, x.split("-"))) for x in self.idRanges]
        self.ingredients = list(map(int, self.ingredients))

    # @answer(615)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((615, 353716783056994))
    def solve(self) -> tuple[int, int]:
        self.preprocess()
        solution1 = solution2 = 0

        stack = []
        self.idRanges.sort()

        for start, end in self.idRanges:
            while stack and start <= stack[-1][1]:
                stackStart, stackEnd = stack.pop()
                start, end = min(start, stackStart), max(end, stackEnd)
            stack.append((start, end))
        

        for start, end in stack:
            solution2 += end - start + 1

        self.idRanges.reverse()

        for ingredient in self.ingredients:
            for start, end in self.idRanges:
                if ingredient >= start and ingredient <= end:
                    solution1 += 1
                    break
        
        return (solution1, solution2)
        
        





    
