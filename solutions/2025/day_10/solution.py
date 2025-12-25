# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque
from math import inf
from itertools import combinations
from numpy import array, int64
from collections import defaultdict


class ComboDict():
    def __init__(self, buttons):
        self.dict = defaultdict(list)
        allCombos = []
        for i in range(1, len(buttons[0] + 1)):
            allCombos.extend([(i, sum(combo)) for combo in combinations(buttons,i)])


        allCombos.sort(key = lambda x: (list(x[1]), x[0]))

        self.stack = [allCombos.pop()]
        for length, combo in allCombos:
            if (combo != self.stack[-1][1]).any():
                self.stack.append((length, combo))

        self.stack.sort(key = lambda x: sum(x[1]))


    def values(self):
        return self.stack





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

    def parseLine2(self, line):
        elements = line.split(" ")
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))
        buttons = []
        for button in elements[1:-1]:
            buttonArray = [0] * len(joltages)
            registersTripped =  map(int, button.strip("()").split(","))
            for reg in registersTripped:
                buttonArray[reg] = 1
            buttons.append(array(buttonArray, dtype=int64))

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


    def recNumPresses(self, stepsTaken, remainingJoltage, comboPointer) -> None:
        print("Remaining Joltage:", remainingJoltage)
        assert(not any([x < 0 for x in remainingJoltage]))

        if stepsTaken >= self.memo[*remainingJoltage] or stepsTaken >= self.shortestPathToZero:
            return

        self.memo[*remainingJoltage] = stepsTaken
            
        remainingJoltage = array(remainingJoltage, dtype=int64)

        if (remainingJoltage == 0).all():
            print("FOUND ZERO")
            self.memo[*remainingJoltage] = stepsTaken
            self.shortestPathToZero = min(self.shortestPathToZero, stepsTaken)
            return

        if comboPointer >= len(self.comboDict.values()):
            return

        
        currSteps, combo = self.comboDict.values()[comboPointer]
        multiplier = 0
        print("Multiplier", multiplier)
        print("Current Combo",self.comboDict.values()[comboPointer])

        while all([a >= b for a, b in zip(remainingJoltage, combo * multiplier)]):
            print("Multiplier", multiplier)
            print("Current Combo",self.comboDict.values()[comboPointer])
            self.recNumPresses(stepsTaken + currSteps * multiplier, remainingJoltage - combo * multiplier, comboPointer + 1)
            multiplier += 1



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
        """
        divisible = array([2, 1, 1, 2])
        badMultiplied = array([2, 2, 4, 4])
        multiplied = array([4, 2, 2, 4])
        divisibleZero = array([0, 1, 1, 2])
        indivisible = array([3, 1, 1, 2])
        combo = array([2, 1, 1, 2])
        comboZero = array([0, 1, 1, 2])
        print(self.divideArray(divisible, combo))
        print(self.divideArray(indivisible, combo))
        print(self.divideArray(indivisible, comboZero))
        print(self.divideArray(divisibleZero, comboZero))
        print(self.divideArray(multiplied, divisible))
        print("Bad multiplier",self.divideArray(badMultiplied, divisible))
        """
        part2answer = 0
        for line in self.input:
            self.shortestPathToZero = inf
            buttons, joltages = self.parseLine2(line)
            self.memo = defaultdict(lambda: inf)
            self.comboDict = ComboDict(buttons)

            self.recNumPresses(0, joltages, 0)
            assert(self.shortestPathToZero) != inf
            part2answer += self.shortestPathToZero


        return part2answer





    # @answer((0, 0))
    # def solve(self) -> tuple[int, int]:
    #   pass 