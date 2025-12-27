# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
from collections import defaultdict

class Device():
    def __init__(self, id):
        self.visited = False
        self.keep = False
        self.id = id
        self.downstream = []
        self.upstream = []

    def __sub__(self, other: "Device"):
        self.downstream.remove(other)
        other.upstream.remove(self)


    def __repr__(self):
        return "({}: ^{} _{})".format(self.id, *[x.id for x in self.upstream] if self.upstream else "xxx", *[x.id for x in self.downstream] if self.downstream else "xxx")

    def __hash__(self):
        return hash(self.id)

class Solution(StrSplitSolution):
    _year = 2025
    _day = 11

    def link(self, a: Device, b: Device):
        a.downstream.append(b)
        b.upstream.append(a)

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
        nodeDict = {}
        for line in self.input:
            id, downstreamNodeIDs = line.split(": ")
            downstreamNodeIDs = downstreamNodeIDs.split(" ")
            print("Upstreamm ID", id)
            if id not in nodeDict:
                nodeDict[id] = Device(id)
            for downstreamID in downstreamNodeIDs:
                print("Downstream ID", downstreamID)
                if downstreamID not in nodeDict:
                    nodeDict[downstreamID] = Device(downstreamID)
                self.link(nodeDict[id], nodeDict[downstreamID])

        print(nodeDict.values())


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
