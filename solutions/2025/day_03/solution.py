# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3

    @answer(17408)
    def part_1(self) -> int:
        largestJoltage = 0
        for bank in self.input:
            tens = "0"
            ones = bank[-1]
            for i in range(len(bank) - 1):
                if bank[i] > tens:
                    tens = bank[i]
                    ones = bank[-1]
                elif bank[i] > ones:
                    ones = bank[i]
            largestJoltage += int(tens + ones)
        return largestJoltage
            

    @answer(172740584266849)
    def part_2(self) -> int:
        largestJoltage = 0
        for bank in self.input:
            q = []
            for i in range(len(bank)):
                while q and bank[i] > q[-1] and len(q) >= max(0,13 - len(bank) + i):
                    q.pop()
                q.append(bank[i])
                print("".join(q[:12]))
            

            assert(len(q)>=12)
            largestJoltage += int("".join(q[:12]))

        return largestJoltage


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
