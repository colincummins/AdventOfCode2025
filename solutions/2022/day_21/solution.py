# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/21

from ...base import StrSplitSolution, answer
import operator
from collections import defaultdict, deque
from heapq import heappush, heappop
from fractions import Fraction
from re import fullmatch

class Monkey():
    def __init__(self, key: str, phrase: str):
        self.key = key
        self.num = None
        self.waiting = []
        self.numDict = defaultdict(lambda: None)

        if bool(fullmatch(r"^-?\d+$", phrase)):
            self.inDegree = 0
            self.num = int(phrase)
            self.operation = None
            self.isNumber = True
        else:
            self.inDegree = 2
            first, self.operation, second = phrase.split(" ")
            self.waiting = [first, second]
            self.setOperator(self.operation)

    @property
    def leftAncestorKey(self):
        return self.waiting[0] if self.waiting else None

    @property
    def rightAncestorKey(self):
        return self.waiting[1] if self.waiting else None

    @property
    def leftVal(self):
        return self.numDict[self.waiting[0]] if self.waiting else None
    
    @leftVal.setter
    def leftVal(self, val):
        self.numDict[self.leftAncestorKey] = val

    @property
    def rightVal(self):
        return self.numDict[self.waiting[1]] if self.waiting else None

    @rightVal.setter
    def rightVal(self, val):
        self.numDict[self.rightAncestorKey] = val

    def setOperator(self, operation: str):
        match operation:
            case "+": 
                self.operation = operator.add
            case "-": 
                self.operation = operator.sub
            case "*": 
                self.operation = operator.mul
            case "/": 
                self.operation = Fraction
            case "=":
                self.operation = self.equalityOperator 


    def equalityOperator(self, *args):
        pass

    def listen(self, key: str, value: int):
        self.numDict[key] = value
        self.inDegree -= 1

        if self.operation == self.equalityOperator:
            self.num = value
        elif self.inDegree == 0:
            self.num = self.operation(self.leftVal, self.rightVal )

    def shout(self) -> tuple[str, int]:
        if self.num is None:
            raise ValueError("Monkey doesn't have needed nums")
        return self.key, self.num

    def __repr__(self):
        return "<name: {} | num: {}>".format(self.key, self.num)

    def __lt__(self, other) -> bool:
        return self.inDegree < other.inDegree

    def solveEquation(self, inherited: int):
        print("{} is solving an equation for {}".format(self, inherited))
        print("{} attributes:".format(vars(self)))
        
        # Check for nodes which are already full resolved = val and both waiting values
        a, b = self.leftVal, self.rightVal

        if self.operation is None or (a is not None and b is not None):
            assert(self.num == inherited)
            self.num = inherited
            print("{} is already solved".format(self))
            return

        self.num = inherited

        print(vars(self))
        print("a: {}, b: {}".format(a, b))
        if a is not None:
            match self.operation:
                case operator.add:
                    # leftside = a + b =>
                    b = inherited - a

                case operator.sub:
                    # leftside = a - b =>
                    b = a - inherited

                case operator.mul:
                    # leftside = a * b =>
                    b = Fraction(inherited, a)

                case _:
                    # leftside = a / b =>
                    b = Fraction(a, inherited)
            self.rightVal = b

        elif b is not None:
            match self.operation:
                # solving for a
                case operator.add:
                    # leftside = a + b =>
                    a = inherited - b

                case operator.sub:
                    # leftside = a - b =>
                    a = b + inherited

                case operator.mul:
                    # leftside = a * b =>
                    a = Fraction(inherited, b)

                case _:
                    # leftside = a / b =>
                    a = inherited * b
            self.leftVal = a

        else:
            raise ValueError("Monkey has no attributes and can't solve")

            print("{} value1 is {}".format(self, getattr(self, self.waiting2)))





class Solution(StrSplitSolution):
    _year = 2022
    _day = 21

        




    # @answer(1234)
    def part_1(self) -> int:
        neighbors = defaultdict(list)
        jungle = {}
        for line in self.input:
            key, phrase = line.split(": ")
            jungle[key] = Monkey(key, phrase)
        for monkey in jungle.values():
            for neighbor in monkey.waiting:
                neighbors[neighbor].append(monkey)

        q = deque(filter(lambda x: x.inDegree == 0, jungle.values()))

        while q:
            curr = q.popleft()
            for neighbor in neighbors[curr.key]:
                neighbor.listen(*curr.shout())
                if neighbor.inDegree == 0:
                    q.append(neighbor)

        return jungle["root"].num


    # @answer(1234)
    def part_2(self) -> int:
        return 0
        ANSWERNODE = "humn"
        neighbors = defaultdict(set)
        jungle = {}
        for line in self.input:
            key, phrase = line.split(": ")
            if key == ANSWERNODE:
                print("Ignoring humn")
                continue
            jungle[key] = Monkey(key, phrase)
        jungle["root"].setOperator("=")
        for monkey in jungle.values():
            for neighbor in monkey.waiting:
                neighbors[neighbor].add(monkey)

        q = deque(filter(lambda x: x.inDegree == 0, jungle.values()))

        while q:
            curr = q.popleft()
            for neighbor in neighbors[curr.key]:
                neighbor.listen(*curr.shout())
                if neighbor.inDegree == 0:
                    q.append(neighbor)


        # create human node to catch answer
        human = Monkey("humn","0 = 0")
        human.operation = None
        human.waiting1 = human.waiting2 = None
        jungle["humn"] = human

        q = deque([jungle["root"]])
        while q:
            curr = q.pop()
            for ancestor in curr.waiting:
                if ancestor is not None:
                    print("{} is calling {}".format(curr, ancestor))
                    ancestor = jungle[ancestor] 
                    ancestor.solveEquation(curr.num)
                    q.append(ancestor)


        return jungle["humn"].num
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
