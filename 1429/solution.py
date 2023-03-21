class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freq = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.head.next == self.tail:
            return -1
        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.freq:
            if self.freq[value] is not None:
                node = self.freq[value]
                node.prev.next = node.next
                node.next.prev = node.prev
                self.freq[value] = None
        else:
            node = Node(value)
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            self.freq[value] = node

class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None