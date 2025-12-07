# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    #@answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        split = 0
        curr = 1 << (70)
        for row in self.input:
            buffer = 0
            for i, node in enumerate(row):
                if node == "^" and (curr & 1 << i):
                    buffer |= (1 << i + 1) 
                    buffer |= (1 << i - 1)
                    curr ^= 1 << i
                    split += 1
            curr |= buffer
            print("current",str(bin(buffer))[2:].zfill(30))
        return (split, 0)

