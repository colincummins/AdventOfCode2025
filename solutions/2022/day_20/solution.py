# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/20

from ...base import IntSplitSolution, answer

class DllNode():
    def __init__(self, originalPos = None, val= None, prev = None, next = None):
        self.originalPos = originalPos
        self.val = val
        self.prev = prev
        self.next = next
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def __hash__(self):
        return self.originalPos

    def __repr__(self):
        return "pos:" + self.originalPos + " val: " + self.val

    def __str__(self):
        return "{}".format(self.val)
    

class DoublyLinkedList():
    def __init__(self, nodevals):
        self.nodes = []
        for i, num in enumerate(nodevals):
            self.nodes.append(DllNode(i, num))

        for i in range(len(self.nodes) - 1):
            self.nodes[i].next = self.nodes[i+1]

        for i in range(1, len(self.nodes)):
            self.nodes[i].prev = self.nodes[i - 1]

        self.nodes[-1].next = self.nodes[0]
        self.nodes[0].prev = self.nodes[-1]

        self.nodeDict = {hash(node): node for node in self.nodes}
        self.head = self.nodes[0]
        self.pointer = self.head
    
    def __str__(self):
        builder = []
        curr = self.head
        for i in range(len(self.nodes)):
            builder.append(str(curr))
            curr = curr.next
        return " <-> ".join(builder)


    def __len__(self) -> int:
        return len(self.nodes)

    def insert(self, nodeToInsert, trailingNode):
        leadingNode = trailingNode.next
        trailingNode.next = nodeToInsert
        nodeToInsert.prev = trailingNode
        leadingNode.prev = nodeToInsert
        nodeToInsert.next = leadingNode

    def shift(self, index: int, offset: int):
        pass

    def find(self, key:int):
        curr = self.head
        while curr.val != key:
            curr = curr.next
        self.pointer = curr
        return curr

    def advance(self, offset:int):
        while offset > 0:
            offset -= 1
            self.pointer = self.pointer.next
        return self.pointer.val

    def pointerVal(self) -> int:
        return self.pointer.val


class Solution(IntSplitSolution):
    _year = 2022
    _day = 20

    # @answer(1234)
    def part_1(self) -> int:
        """
        nodes = DoublyLinkedList([1, 2, 3])
        print(nodes)
        nodes.shift(0, 1)
        print(nodes)
        """
        part1 = 0
        nodes = DoublyLinkedList(self.input)
        assert(all([node.val == num for node, num in zip(nodes.nodes, self.input)]))
        for i in range(len(self.input)):
            nodes.shift(i, self.input[i])
        nodes.find(0)
        for i in range(3):
            part1 += nodes.advance(1000)
            print(nodes.pointer)

        return part1

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
