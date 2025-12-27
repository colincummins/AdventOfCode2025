# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
from collections import defaultdict
from functools import cache

class Solution(StrSplitSolution):
    _year = 2025
    _day = 11

    @answer(470)
    def part_1(self) -> int:
        downstreamDict = {}
        visited = set()
        self.paths = 0
        for line in self.input:
            node, downstreamNodes = line.split(": ")
            downstreamDict[node] = list(downstreamNodes.split(" "))

        def aux(node: str) -> None:
            if node in visited:
                return

            visited.add(node)

            if node == "out":
                self.paths += 1

            else:
                for downstream in downstreamDict[node]:
                    aux(downstream)

            visited.remove(node)

        aux("you")
        return self.paths



    # @answer(1234)
    def part_2(self) -> int:
        part2answer = 0
        downstreamDict = defaultdict(list)
        for line in self.input:
            node, downstreamNodes = line.split(": ")
            downstreamDict[node] = list(downstreamNodes.split(" "))

        @cache
        def aux(curr: str, dest:str) -> int:
            if curr == dest:
                return 1

            answer = 0

            for next in downstreamDict[curr]:
                answer += aux(next, dest)

            return answer

        svrTOfft = aux("svr", "fft")
        aux.cache_clear()
        fftTOdac = aux("fft", "dac")
        aux.cache_clear()
        dacTOout = aux("dac", "out")

        return svrTOfft * fftTOdac * dacTOout



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
