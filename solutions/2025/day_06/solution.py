# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from ...base import StrSplitSolution, answer
from re import split
from operator import add, mul


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6

    @answer(4771265398012)
    def part_1(self) -> int:
        operators = [add if x == "+" else mul for x in self.input.pop().split()]
        accumulator = map(int,self.input.pop().split())
        while self.input:
            current = map(int,self.input.pop().split())
            accumulator = map(lambda a, b, opp: opp(a,b), accumulator, current, operators)
        return sum(accumulator)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
