# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from collections import namedtuple
from dataclasses import dataclass
from functools import cache

@dataclass(frozen=True)
class Point():
    x: int
    y: int


class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    def parseInput(self):
        self.input = [Point(*map(int, row.split(","))) for row in self.input]

    def getRectangleArea(self, pt1: Point, pt2: Point) -> int:
        return (abs(pt1.x - pt2.x) + 1) * (abs(pt1.y - pt2.y) + 1)

    def createPointFromIndex(self, xIndex: int, yIndex: int) -> Point:
        return Point(self.xCoords[xIndex], self.yCoords[yIndex])
    
    @cache
    def recFindRectangles(self, upper: int, lower: int, left: int, right: int) -> int:
        hash = (upper, lower, left, right)

        if self.memo.get(hash) is not None:
            return self.memo.get(hash)


        upperLeft = self.createPointFromIndex(left, upper)
        lowerRight = self.createPointFromIndex(right, lower)
        opposite1 = set([upperLeft, lowerRight])
        lowerLeft = self.createPointFromIndex(left, lower)
        upperRight = self.createPointFromIndex(right, upper)
        opposite2 = set([lowerLeft, upperRight])

        if upper > lower or left > right or (self.memo.values() and self.getRectangleArea(upperLeft, lowerRight) < max(self.memo.values())):
            self.memo[hash] = 0
            return 0


        if opposite1.issubset(self.allRedTiles) or opposite2.issubset(self.allRedTiles):
            self.memo[hash] = self.getRectangleArea(upperLeft, lowerRight)
            print(self.memo[hash])
            return self.memo[hash]

        bestRectangle = max([
        self.recFindRectangles(upper + 1, lower, left, right),
        self.recFindRectangles(upper, lower - 1, left, right),
        self.recFindRectangles(upper, lower, left + 1, right),
        self.recFindRectangles(upper, lower, left, right - 1)])

        self.memo[hash] = bestRectangle
        return bestRectangle


    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        self.memo = {}
        self.maxRect = 0
        self.parseInput()
        self.allRedTiles = set()
        self.xCoords = set()
        self.yCoords = set()
        for coord in self.input:
            self.allRedTiles.add(coord)
            self.xCoords.add(coord.x)
            self.yCoords.add(coord.y)
        self.xCoords = sorted(self.xCoords)
        self.yCoords = sorted(self.yCoords)

        return (self.recFindRectangles(0, len(self.yCoords) - 1, 0, len(self.xCoords) - 1), 0)


            

            




