# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from itertools import combinations
from shapely import Point, Polygon, MultiPoint, envelope






class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    @staticmethod
    def getBoxVolume(box: Polygon)->int:
        minx, miny, maxx, maxy = box.bounds
        return (maxx - minx + 1) * (maxy - miny + 1)


    def parseInput(self):
        self.input = [Point(*map(int, row.split(","))) for row in self.input]

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        part1 = 0
        part2 = 0
        self.parseInput()
        tilePattern = Polygon(self.input)
        for a, b in combinations(self.input, 2):
            currBox = envelope(MultiPoint([a, b]))
            currVolume = self.getBoxVolume(currBox)
            if currVolume > part1:
                part1 = currVolume
            if tilePattern.contains(currBox) and currVolume > part2:
                part2 = currVolume
        

        return (int(part1), int(part2))
        


            




