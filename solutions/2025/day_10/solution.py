# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    def printReg(self, register):
        return "".join(map(lambda x: "." if x == "0" else "#", reversed(bin(register)[2:])))

    def parseLine(self, line):
        elements = line.split(" ")
        lights = int("".join(map(lambda x: "1" if x=="#" else "0", elements[0].strip("[]")[::-1])),2)
        buttons = []
        for button in elements[1:-1]:
            val = 0
            for reg in map(int, button.strip("()").split(",")):
                val |= 1 << reg
            buttons.append(val)
        joltages = map(int, elements[-1].strip("{}").split(","))

        return lights, buttons, joltages




    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        """
        reg = Register([0, 1, 4])
        reg2 = Register([])
        print(reg)
        print(reg2)
        reg2 ^= reg
        print(reg)
        print(reg2)
        reg2 ^= reg
        print(reg2)
        """
        totalPresses = 0
        for line in self.input:
            self.debug("New Line:")
            lights, buttons, joltages = self.parseLine(line)
            self.debug("Lights:", lights, "Buttons:", buttons, "Joltages:", *joltages)
            visited = set()
            q = deque([(0, 0)])
            while q:
                self.debug(q)
                steps, curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == lights:
                    self.debug(steps)
                    totalPresses += steps
                    break
                for button in buttons:
                    q.append((steps + 1, button ^ curr))

        return (totalPresses, 0)

