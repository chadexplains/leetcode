class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % len(self.queue)
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)