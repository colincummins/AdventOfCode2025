# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ','
    def parseInputToRanges(self):
        ranges = [x.split("-") for x in self.input]
        ranges = [(int(x[0]), int(x[1])) for x in ranges]
        self.input = ranges
        return

    # @answer(1234)
    def part_1(self) -> int:
        result = 0
        s = 1
        self.parseInputToRanges()
        self.input.sort(reverse=True)
        self.input1 = self.input[:]

        while self.input1:
            lower, upper = self.input1[-1]
            candidate = int(str(s) + str(s))
            if candidate > upper:
                self.input1.pop()
                continue
            if candidate >= lower and candidate <= upper:
                result += candidate
            s += 1
        
        return result



    # @answer(1234)
    def part_2(self) -> int:
        result = 0
        candidates = set()
        upperLimit = self.input[0][1]
        print(upperLimit)
        for s in range(1, 99999):
            pattern = str(s)
            candidate = pattern * 2
            while int(candidate) <= upperLimit:
                candidates.add(int(candidate))
                candidate = candidate + pattern
        
        
        candidates = list(candidates)
        candidates.sort(reverse = True)
        print(candidates[0])

        while self.input and candidates:
            lower, upper = self.input[-1]
            if candidates[-1] > upper:
                self.input.pop()
            elif candidates[-1] >= lower and candidates[-1] <= upper:
                result += candidates.pop()
            elif candidates[-1] < lower:
                candidates.pop()
        
        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
