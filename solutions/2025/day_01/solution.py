# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        password = 0
        dial = 50
        for comboStr in self.input:
            combo = int(comboStr[1:])
            if comboStr[0] == "R":
                combo *= -1
            dial += combo
            dial %= 100
            if dial == 0:
                password += 1
        return password

    # @answer(1234)
    def part_2(self) -> int:
        password = 0
        dial = 50
        for comboStr in self.input:
            combo = int(comboStr[1:])
            password += combo // 100
            combo %= 100
            if comboStr[0] == "L":
                combo *= -1
            newDial = dial + combo
            if (dial !=0) and (newDial <= 0 or newDial >= 100):
                password += 1 
            dial = (newDial + 100) % 100
        return password

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
