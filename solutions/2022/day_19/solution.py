# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/19

from ...base import StrSplitSolution, answer
from re import findall
from functools import cache
from math import ceil


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



            # Wait and build orebot
            if oreBot < max(obsidianRobotOreCost, geodeRobotOreCost, clayRobotCost):
                turnsNeeded = max(0,ceil((oreRobotCost - ore) / oreBot)) + 1
                scenarios.append(tryBlueprint(oreBot + 1, clayBot, obsidianBot, geodeBot, ore + (turnsNeeded * oreBot) - oreRobotCost, clay + turnsNeeded * clayBot, obsidian + turnsNeeded * obsidianBot, geodes + geodeBot * turnsNeeded, turns + turnsNeeded))

            # Wait and build claybot
            if oreBot and clayBot < obsidianRobotClayCost:
                turnsNeeded = max(0, ceil((clayRobotCost - ore) / oreBot)) + 1
                scenarios.append(tryBlueprint(oreBot, clayBot + 1, obsidianBot, geodeBot, ore + (turnsNeeded * oreBot)- clayRobotCost, clay + turnsNeeded * clayBot, obsidian + turnsNeeded * obsidianBot, geodes + geodeBot * turnsNeeded, turns + turnsNeeded))


            # Wait and build obsidianbot
            if oreBot and clayBot and obsidianBot < geodeRobotObsidianCost:
                turnsNeeded = max(0, ceil((obsidianRobotOreCost - ore) / oreBot), ceil((obsidianRobotClayCost - clay)/clayBot)) + 1
                scenarios.append(tryBlueprint(oreBot, clayBot, obsidianBot + 1, geodeBot, ore + (turnsNeeded * oreBot)- obsidianRobotOreCost, clay + (turnsNeeded * clayBot) - obsidianRobotClayCost, obsidian + turnsNeeded * obsidianBot, geodes + geodeBot * turnsNeeded, turns + turnsNeeded))

            # Wait and build geodebot
            if oreBot and obsidianBot:
                turnsNeeded = max(0, ceil((geodeRobotOreCost - ore) / oreBot), ceil((geodeRobotObsidianCost - obsidian)/obsidianBot)) + 1
                scenarios.append(tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot + 1, ore + (turnsNeeded * oreBot)- geodeRobotOreCost, clay + turnsNeeded * clayBot, obsidian + turnsNeeded * obsidianBot - geodeRobotObsidianCost, geodes + geodeBot * turnsNeeded, turns + turnsNeeded))

            # Wait until last turn
            if geodeBot:
                turnsNeeded = TURN_LIMIT - turns
                scenarios.append(tryBlueprint(oreBot, clayBot, obsidianBot, geodeBot, ore + (turnsNeeded * oreBot), clay + turnsNeeded * clayBot, obsidian + turnsNeeded * obsidianBot, geodes + geodeBot * turnsNeeded, turns + turnsNeeded))


            return max(scenarios)
            
        part1 = 0
        TURN_LIMIT = 25
        for line in self.input:
            tryBlueprint.cache_clear()
            blueprintNum, oreRobotCost, clayRobotCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = self.extractNums(line)
            buildResult = tryBlueprint(1, 0, 0, 0, 0, 0, 0, 0, 1) 
            print("Blueprint: ", blueprintNum, " resulted in", buildResult, " geodes")
            part1 += buildResult * blueprintNum

        part2 = 1
        TURN_LIMIT = 33
        for line in self.input[:3]:
            tryBlueprint.cache_clear()
            blueprintNum, oreRobotCost, clayRobotCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = self.extractNums(line)
            buildResult = tryBlueprint(1, 0, 0, 0, 0, 0, 0, 0, 1) 
            print("Blueprint: ", blueprintNum, " resulted in", buildResult, " geodes")
            part2 *= buildResult

        return part1, part2