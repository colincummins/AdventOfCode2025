# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
from collections import deque, defaultdict
from heapq import heappush, heappop
from math import inf


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
        joltages = tuple(map(int, elements[-1].strip("{}").split(",")))

        return lights, buttons, joltages

    def parseInput(self):
        self.input = [self.parseLine(line) for line in self.input]

    def getAstar(self, joltages: tuple[int]) -> int:
        return (sum(map(lambda x: x**2, joltages)))**(1/len(joltages))




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
        for lights, buttons, joltages in self.input:
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
                    part1 += steps
                    break
                for button in buttons:
                    q.append((steps + 1, button ^ curr))

        #part 2
        part2 = 0
        for _, buttons, joltages in self.input:
            self.debug("New Line:")
            visited = set()

            dist = defaultdict(lambda: inf)
            astar = defaultdict(lambda: inf)

            dist[joltages] = 0
            astar[joltages] = self.getAstar(joltages)

            # AStar Distance, Current Distance, Joltages
            heap = [(0, 0, tuple(joltages))]
            visited = set()

            while heap:
                self.debug("Lights:", lights, "Buttons:", buttons, "Joltages:", *joltages)
                currAStar, currDist, joltages = heappop(heap)
                visited.add(joltages)
                if all(x == 0 for x in joltages):
                    part2 += currDist
                    break
                for button in buttons:
                    neighbor = list(joltages)
                    digit = 0
                    while button != 0:
                        self.debug("Button:", button)
                        if button & 1:
                            neighbor[digit] -= 1
                        button >>= 1 
                        digit += 1
                    if any(x < 0 for x in neighbor):
                        continue
                    neighbor = tuple(neighbor)
                    if dist[joltages] + 1 < dist[neighbor]:
                        dist[neighbor] = dist[joltages] + 1
                        astar[neighbor] = dist[joltages] + 1 + self.getAstar(neighbor)
                        if neighbor not in visited:
                            heappush(heap, (astar[neighbor], dist[neighbor], neighbor))





            # Remember - no negative joltages allowed


        return (part1, part2)

