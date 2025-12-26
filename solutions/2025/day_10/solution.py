# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque
from math import inf
from itertools import combinations
from numpy import array, int64
from collections import defaultdict
from functools import cache


class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    def createComboDict(self, buttons):
        dict = defaultdict(list)
        allCombos = []
        for i in range(1, len(buttons[0] + 1)):
            allCombos.extend([(i, *sum(combo)) for combo in combinations(buttons,i)])
        
        allCombos.sort()

        for steps, *combo in allCombos:
            dict[*(int(x) % 2 for x in combo)].append((steps, *combo))

        print("Dictionary Created:")
        print(*dict.items(), sep = "\n")

        return dict




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

    def parseLine2(self, line):
        elements = line.split(" ")
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))
        buttons = []
        for button in elements[1:-1]:
            buttonArray = [0] * len(joltages)
            registersTripped =  map(int, button.strip("()").split(","))
            for reg in registersTripped:
                buttonArray[reg] = 1
            buttons.append(array(buttonArray))

        return buttons, joltages

    @staticmethod
    def divideArray(num, denom):
        factors = []
        for a, b in zip(num, denom):
            if a != 0 and b == 0:
                return 0

            if a and a % b != 0:
                return 0

            if a < b:
                return 0
                
            if a and b:
                factors.append(a//b)

        if len(set(factors)) == 1:
            return factors[0]

        return 0

    @cache
    def recNumPresses(self, remainingJoltage) -> int:
        remainingJoltage = array(remainingJoltage)
        print("Remaining Joltage:", remainingJoltage)
        assert(not any([x < 0 for x in remainingJoltage]))

        presses = inf

        if (remainingJoltage == 0).all():
            return 0

        for steps, *combo in self.comboDict[tuple((remainingJoltage%2))]:
            print("Might take {} steps with combo {}".format(steps,combo))
            if (remainingJoltage >= combo).all():
                print("Reduced:", (remainingJoltage - combo))
                presses = min(presses, steps + 2 * self.recNumPresses(tuple([(a - b)//2 for a, b in zip(remainingJoltage, combo)])))

        print("Steps:", presses)
        return presses

            

    @answer(401)
    def part_1(self) -> int:
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
        return part1

    # @answer(1234)
    def part_2(self) -> int:
        part2answer = 0
        for line in self.input:
            self.recNumPresses.cache_clear()
            buttons, joltages = self.parseLine2(line)
            self.comboDict = self.createComboDict(buttons)
            part2answer += self.recNumPresses(joltages)

        return part2answer







    # @answer((0, 0))
    # def solve(self) -> tuple[int, int]:
    #   pass 