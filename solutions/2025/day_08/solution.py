# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

from ...base import StrSplitSolution, answer
from math import sqrt
from functools import reduce

class UnionFind():
    def __init__(self, elements):
        self.parent = {element:element for element in elements}
        self.size = {element:1 for element in elements}

    def find(self, key):
        curr = key
        while self.parent[curr] != curr:
            curr = self.parent[curr]

        while key is not curr:
            next = self.parent[key]
            self.parent[key] = curr
            key = next

        return self.parent[key]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.parent[y] = x
        return self.size[x]

class Solution(StrSplitSolution):
    _year = 2025
    _day = 8
    def parseInput(self):
        self.input = [tuple(map(int, x.split(","))) for x in self.input]

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((123420, 673096646))
    def solve(self) -> tuple[int, int]:
        self.parseInput()
        uf = UnionFind(self.input)
        """
        assert(uf.find(self.input[0])==self.input[0])
        uf.union(self.input[0], self.input[1])
        assert(uf.find(self.input[0]) == uf.find(self.input[1]))
        print(uf.size)
        """
        distances = []
        for i in range(len(self.input) - 1):
            for j in range(i + 1,len(self.input)):
                a1, a2, a3 = self.input[i]
                b1, b2, b3 = self.input[j]
                dist = sqrt((a1 - b1)**2 + (a2 - b2)**2 + (a3 - b3)**2)
                distances.append((dist, self.input[i], self.input[j]))
        distances.sort()

        cordsUsed = 0
        for dist, x, y in distances:
            cordsUsed += 1
            connected = uf.union(x, y)
            if cordsUsed == 1000:
                part1 =reduce(lambda x, y: x * y, sorted(uf.size.values(), reverse = True)[:3]) 
            if connected == len(self.input):
                part2 = x[0] * y[0]

        return (part1, part2)

        

        
