# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
from collections import defaultdict


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
        downstreamDict = defaultdict(set)
        upstreamDict = defaultdict(set)
        visited = set()
        self.paths = 0
        for line in self.input:
            node, downstreamNodes = line.split(": ")
            downstreamDict[node].update(downstreamNodes.split(" "))
            for successor in downstreamNodes:
                upstreamDict[successor].add(node)
            
        print(downstreamDict)

        

        def aux(node: str, dest: str, dict) -> None:
            if node in visited:
                return

            visited.add(node)

            if node == dest:
                self.paths += 1

            else:
                for nextNode in dict[node]: 
                    aux(nextNode, dest, dict)

            visited.remove(node)

        aux("you", "out", downstreamDict)

        """
        svr -> dac ???
        svr -> fft ???
        dac -> out 8281
        fft -> out ???
        dac -> fft 0
        fft -> dac ???

        O   svr->fft->dac->out
        x   svr->dac->fft->out  (because there are no paths from dac to fft)
        """
        return self.paths

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
