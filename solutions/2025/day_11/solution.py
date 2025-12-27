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
        dontPrune = set()
        visited = set()
        self.paths = 0
        for line in self.input:
            node, downstreamNodes = line.split(": ")
            downstreamDict[node].update(downstreamNodes.split(" "))
            for successor in downstreamNodes.split():
                upstreamDict[successor].add(node)
        print("Downstream:") 
        print(*downstreamDict.items(), sep="\n")
        print("Upstream:") 
        print(*upstreamDict.items(), sep="\n")

        

        def aux(node: str, dest: str, dict, dontPrune = set()) -> None:
            if node in visited:
                return

            visited.add(node)

            if node == dest:
                dontPrune |= visited
                dontPrune.add(dest)
                self.paths += 1

            else:
                for nextNode in dict[node]: 
                    aux(nextNode, dest, dict, dontPrune)

            visited.remove(node)

        def prune(node: str, dest: str, dict, dontPrune) -> None:
            if node in visited:
                return

            visited.add(node)

            if node != dest:
                for next in dict[node]:
                    if next not in dontPrune:
                        print("Pruned")
                        dict[node].remove(next)
                    else:
                        prune(node, dest, dict, dontPrune)


            visited.remove(node)


        aux("dac", "out", downstreamDict, dontPrune) 
        print(dontPrune)
        prune("dac", "out", downstreamDict, dontPrune)
        dontPrune = set()
        self.paths = 0
        aux("fft", "svr", upstreamDict, dontPrune)
        print(dontPrune)
        prune("svr", "fft", downstreamDict, dontPrune)
        print(dontPrune)
        prune("fft", "svr", upstreamDict, dontPrune)
        self.paths = 0
        print(self.paths)


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

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
