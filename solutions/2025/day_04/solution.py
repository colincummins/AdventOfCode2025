# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from ...base import StrSplitSolution, answer
from collections import deque

class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    def getNeighbors(self, r, c):
        neighbors = []
        ADJACENT = [[1, -1],[1, 0],[1, 1],[0, -1],[0, 1],[-1, -1],[-1, 0],[-1, 1]]
        for deltaR, deltaC in ADJACENT:
            newR, newC = r + deltaR, c + deltaC 
            if self.isValidCoord(newR, newC):
                neighbors.append((newR, newC))
        return neighbors

    def initialize_grid(self):
        self.grid = [list(map(lambda x: 0 if x=="@" else ".", list(row))) for row in self.input]
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c]==0:
                    for newR, newC in self.getNeighbors(r, c):
                        if self.grid[newR][newC] != ".":
                            self.grid[r][c] += 1

    
    def isValidCoord(self, r, c) -> bool:
        return r >=0 and r < len(self.grid) and c >= 0 and c < len(self.grid[0])

    @answer(1505)
    def part_1(self) -> int:
        pass

    @answer(9182)
    def part_2(self) -> int:
        pass 


    @answer((1505, 9182))
    def solve(self) -> tuple[int, int]:
        part2 = 0
        q = deque()
        self.initialize_grid()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c]!="." and self.grid[r][c]<4:
                    q.append((r, c))

        part1 = len(q)
        
        while q:
            r, c = q.popleft()
            if self.grid[r][c] != ".":
                self.grid[r][c] = "."
                part2 += 1
                for newR, newC in self.getNeighbors(r, c):
                    if self.grid[newR][newC] != ".":
                        self.grid[newR][newC] -= 1
                        if self.grid[newR][newC] < 4:
                            q.append((newR, newC))

        return (part1, part2)
                    
        

