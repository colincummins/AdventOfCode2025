# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 5

    def preprocess(self) -> None:
        splitIndex = self.input.index("")
        self.idRanges, self.ingredients = self.input[0:splitIndex], self.input[splitIndex + 1:]
        self.idRanges = [list(map(int, x.split("-"))) for x in self.idRanges]
        self.ingredients = list(map(int, self.ingredients)

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:
        solution1 = solution2 = 0
        self.preprocess()
        
        prefixSum = [0] * (max(self.ingredients) + 2)
        for start, end in self.idRanges:
            prefixSum[start] += 1
            prefixSum[end + 1] -=1

        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]

        for ingredient in self.ingredients:
            solution1 += prefixSum[ingredient] > 0

        return (solution1, solution2)





    
