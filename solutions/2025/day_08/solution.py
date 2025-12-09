# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

from ...base import StrSplitSolution, answer
from math import sqrt, prod
from heapq import heapify, heappop
from itertools import combinations
from dataclasses import dataclass

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

@dataclass(frozen=True)
class Point():
    x: int
    y: int
    z: int

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5

@dataclass(frozen=True)
class Pair():
    a: Point
    b: Point

    def __post_init__(self):
        self.dist = self.a - self.b

    def __hash__(self):
        return (self.dist, self.a, self.b)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 8
    def parseInput(self):
        self.input = [Point(*map(int, x.split(","))) for x in self.input]

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((123420, 673096646))
    def solve(self) -> tuple[int, int]:
        part1 = part2 = 0
        self.parseInput()
        uf = UnionFind(self.input)

        distances = [(a - b, a, b) for a, b in combinations(self.input, 2)]
        heapify(distances)

        cordsUsed = 0
        while distances and not (part1 and part2):
            _, a, b = heappop(distances)
            cordsUsed += 1
            connected = uf.union(a, b)
            if cordsUsed == 1000:
                part1 =prod(sorted(uf.size.values(), reverse = True)[:3])
            if connected == len(self.input):
                part2 = a.x * b.x

        return (part1, part2)

        

        
