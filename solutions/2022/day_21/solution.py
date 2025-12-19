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
        self.waiting1 = self.waiting2 = None

        if bool(fullmatch(r"^-?\d+$", phrase)):
            self.inDegree = 0
            self.num = int(phrase)
            self.waiting1 = self.waiting2 = None
            self.operator = None
            self.isNumber = True
            return

        self.inDegree = 2
        self.waiting1, self.operation, self.waiting2 = phrase.split(" ")
        self.setOperator(self.operation)

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
        self.__setattr__(key, value)
        self.inDegree -= 1

        if self.operation == self.equalityOperator:
            self.num = value
        elif self.inDegree == 0:
            self.num = self.operation(self.__getattribute__(self.waiting1), self.__getattribute__(self.waiting2))

    def shout(self) -> tuple[str, int]:
        if self.num is None:
            raise ValueError("Monkey doesn't have needed nums")
        return self.key, self.num

    def getWaiting(self) -> tuple[str, str]:
        return (self.waiting1, self.waiting2) if self.waiting1 and self.waiting2 else [] 

    def __repr__(self):
        return self.key

    def __lt__(self, other) -> bool:
        return self.inDegree < other.inDegree

    def solveEquation(self, leftSide: int):
        print("{} is solving an equation for {}".format(self, leftSide))
        print("{} attributes:".format(vars(self)))
        if self.waiting1 is None and self.waiting2 is None:
            print("{} is already solved".format(self))
            return

        if self.num is None:
            self.num = leftSide
        print(vars(self))
        a, b = getattr(self, self.waiting1, None), getattr(self, self.waiting2, None)
        print("a, b",a, b)
        if a is not None:
            match self.operation:
                # leftSide = self.waiting2 + x -> x = leftSide - self.waiting2
                case operator.add:
                    b = leftSide - a

                # leftSide = self.waiting2 - x -> x = self.waiting2 - leftSide
                case operator.sub:
                    b = a - leftSide

                # leftSide = self.waiting2 * x -> x = leftSide / self.waiting2
                case operator.mul:
                    b = Fraction(leftSide, a)

                # leftSide = self.waiting2 / x -> x = self.waiting1 / leftSide
                case operator.truediv:
                    b = Fraction(a, leftSide)
            setattr(self, self.waiting2, b)
            print("{} resolved to {}".format(self.waiting2,getattr(self, self.waiting2)))

        elif b is not None:
            match self.operation:
                # leftSide = self.waiting2 + x -> x = leftSide - self.waiting2
                case operator.add:
                    a = leftSide - b

                # leftSide = self.waiting2 - x -> x = self.waiting2 - leftSide
                case operator.sub:
                    a = b - leftSide

                # leftSide = self.waiting2 * x -> x = leftSide / self.waiting2
                case operator.mul:
                    a = Fraction(leftSide, b)

                # leftSide = self.waiting2 / x -> x = self.waiting1 / leftSide
                case operator.truediv:
                    a = Fraction(b, leftSide)
            setattr(self, self.waiting1, a)
            print("{} resolved to {}".format(self.waiting1,getattr(self, self.waiting1)))

        else:
            raise ValueError("Monkey has no attributes and can't solve")

            print("{} value1 is {}".format(self, getattr(self, self.waiting2)))

        self.inDegree -= 1
        assert(self.num is not None)
        assert(self.key != "humn")





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
            for neighbor in monkey.getWaiting():
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
        neighbors = defaultdict(set)
        jungle = {}
        for line in self.input:
            key, phrase = line.split(": ")
            jungle[key] = Monkey(key, phrase)
        jungle["root"].setOperator("=")
        for monkey in jungle.values():
            for neighbor in monkey.getWaiting():
                neighbors[neighbor].add(monkey)

        jungle["humn"].inDegree = float("inf")

        q = deque(filter(lambda x: x.inDegree == 0, jungle.values()))
        print(q)

        while q:
            curr = q.pop()
            for neighbor in neighbors[curr.key]:
                print("{} shouts {} to {}".format(*curr.shout(), neighbor.key))
                neighbor.listen(*curr.shout())
                if neighbor.inDegree == 0:
                    print("Neighbor {} has calculated their number: {}".format(neighbor.key, neighbor.num))
                    q.append(neighbor)

        print("root has a value of {}. Attempting to resolve...".format(jungle["root"].num))

        heap = [jungle["root"]]
        print(vars(jungle["root"]))

        while heap:
            curr = heap.pop()
            print("Popped {} from heap".format(curr))
            print(vars(curr))
            assert(curr.num is not None)
            for neighbor in [curr.waiting1, curr.waiting2]:
                if neighbor is not None:
                    neighbor = jungle[neighbor]
                    print("{} interacting with {}".format(curr, neighbor))
                    if neighbor.inDegree > 0:
                        print("{} is passing {} to {} for a solution".format(curr, curr.num, neighbor))
                        neighbor.solveEquation(curr.num)
                        heappush(heap, neighbor)
                    print(heap)

        print("Final queue:", q)
        print("root:",vars(jungle["root"]))
        print("humn:",vars(jungle["humn"]))



        return jungle["humn"].num

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
