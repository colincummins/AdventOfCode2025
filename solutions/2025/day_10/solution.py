# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque, defaultdict
from heapq import heappush, heappop
from math import inf
from functools import cache


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    def printReg(self, register):
        return "".join(map(lambda x: "." if x == "0" else "#", reversed(bin(register)[2:])))

    def parseLine1(self, line):
        elements = line.split(" ")
        lights = int("".join(map(lambda x: "1" if x=="#" else "0", elements[0].strip("[]")[::-1])),2)
        buttons = []
        for button in elements[1:-1]:
            val = 0
            for reg in map(int, button.strip("()").split(",")):
                val |= 1 << reg
            buttons.append(val)
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))

        return lights, buttons, joltages


    def getAstar(self, joltages: tuple[int]) -> int:
        return (sum(map(lambda x: x**2, joltages)))**(1/len(joltages))




    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((401, 0))
    def solve(self) -> tuple[int, int]:
        part1 = 0
        for line in self.input:
            lights, buttons, joltages = self.parseLine1(line)
            visited = set()
            q = deque([(0, 0)])
            while q:
                steps, curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == lights:
                    part1 += steps
                    break
                for button in buttons:
                    q.append((steps + 1, button ^ curr))

        #part 2

        part2 = 0
        for line in self.input:
            self.debug(line)
        """
        @cache
        def recNumPresses(remainingJoltage: tuple[int]) -> int:
            if any([x < 0 for x in remainingJoltage]):
                return inf
            if all([x == 0 for x in remainingJoltage]):
                return 0


        assert recNumPresses((0,0,0,0)) == 0
        assert recNumPresses((-1,0,0,0)) == inf
        for _, buttons, joltages in self.input:
            recNumPresses.cache_clear()
            self.debug("New Line:")
            self.debug("Buttons{}".format(buttons))





            # Remember - no negative joltages allowed
        """


        return (part1, part2)

