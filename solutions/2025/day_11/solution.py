# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
import networkx
from itertools import chain


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
        G = networkx.DiGraph()
        for line in self.input:
            node, downstream = line.split(": ")
            for next in downstream.split(" "):
                G.add_edge(node, next)

        goodNodes = set(chain.from_iterable(networkx.all_simple_paths(G, "dac", "out")))
        outEdges = G.out_edges(goodNodes)
        networkx.is_directed_acyclic_graph(G)
        return len(*networkx.all_simple_paths(G,"svr","fft")) * len(*networkx.all_simple_paths(G,"fft","dac")) * len(*networkx.all_simple_paths(G,"dac","out"))



        




    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
