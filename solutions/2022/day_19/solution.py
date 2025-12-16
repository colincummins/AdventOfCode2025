# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/19

from ...base import StrSplitSolution, answer
from re import findall
from functools import cache


class Solution(StrSplitSolution):
    _year = 2022
    _day = 19
    def extractNums(self, s) -> list[int]:
        pattern = r'\d+'
        return list(map(int,findall(pattern, s)))

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    def solve(self) -> tuple[int, int]:

        @cache
        def tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geodes, turns) -> int:
            assert(all([x >= 0 for x in [ore, clay, obsidian, geodes]]))
            if turns == TURN_LIMIT:
                return geodes

            if turns > TURN_LIMIT:
                return 0

            if geodeRobotOreCost <= ore and geodeRobotObsidianCost <= obsidian:
                return tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot + 1, ore + oreBot - geodeRobotOreCost, clay + clayBot, obsidian + obsidianBot - geodeRobotObsidianCost, geodes + geodeBot, turns + 1)


            scenarios = [0]

            if ore >= oreRobotCost and oreBot <= max(obsidianRobotOreCost, geodeRobotOreCost):
                scenarios.append(tryBlueprint(oreBot + 1, clayBot, obsidianBot, geodeBot, ore + oreBot - oreRobotCost, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1))

            if ore >= clayRobotCost and clayBot <= obsidianRobotClayCost:
                scenarios.append(tryBlueprint(oreBot, clayBot + 1, obsidianBot, geodeBot, ore + oreBot - clayRobotCost, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1))

            if ore >= obsidianRobotOreCost and clay >= obsidianRobotClayCost and obsidianBot <= geodeRobotObsidianCost:
                scenarios.append(tryBlueprint(oreBot, clayBot, obsidianBot + 1, geodeBot, ore + oreBot - obsidianRobotOreCost, clay + clayBot - obsidianRobotClayCost, obsidian + obsidianBot, geodes + geodeBot, turns + 1))

            # Wait and build orebot

            # Wait and build claybot

            # Wait and build obsidianbot

            # Wait and build geodes
            if (clayBot == 0) or (ore < maxOreCost and oreBot < maxOreCost) or (clay < maxClayCost and clayBot < maxClayCost) or (obsidianBot and obsidian < maxObsidianCost and obsidianBot < maxObsidianCost):
                scenarios.append(tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot, ore + oreBot, clay + clayBot, obsidian + obsidianBot, geodes + geodeBot, turns + 1))

            return max(scenarios)
            
        part1 = 0
        TURN_LIMIT = 25
        for line in self.input:
            tryBlueprint.cache_clear()
            blueprintNum, oreRobotCost, clayRobotCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = self.extractNums(line)
            maxOreCost = max(oreRobotCost, clayRobotCost, obsidianRobotOreCost, geodeRobotOreCost)
            maxClayCost = obsidianRobotClayCost
            maxObsidianCost = geodeRobotObsidianCost

            buildResult = tryBlueprint(1, 0, 0, 0, 0, 0, 0, 0, 1) 
            print("Blueprint: ", blueprintNum, " resulted in", buildResult, " geodes")
            part1 += buildResult * blueprintNum

        part2 = 1
        """
        TURN_LIMIT = 32
        for line in self.input[:3]:
            tryBlueprint.cache_clear()
            blueprintNum, oreRobotCost, clayRobotCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = self.extractNums(line)
            maxOreCost = max(oreRobotCost, clayRobotCost, obsidianRobotOreCost, geodeRobotOreCost)
            maxClayCost = obsidianRobotClayCost
            maxObsidianCost = geodeRobotObsidianCost

            buildResult = tryBlueprint(1, 0, 0, 0, 0, 0, 0, 0, 1) 
            print("Blueprint: ", blueprintNum, " resulted in", buildResult, " geodes")
            part2 *= buildResult
            """
        return part1, part2