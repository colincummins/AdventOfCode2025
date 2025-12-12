# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from collections import namedtuple
from dataclasses import dataclass
from functools import cache
from math import sqrt, atan2
from ...utils.vectors import Point 
from itertools import combinations




class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    def parseInput(self):
        self.input = [Point(*map(int, row.split(","))) for row in self.input]

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        part1 = 0
        self.parseInput()
        for a, b in combinations(self.input, 2):
            part1 = max(part1, a.getRectArea(b))
        
        return (part1,0)
        


            




