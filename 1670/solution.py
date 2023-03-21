class FrontMiddleBackQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def pushFront(self, val: int) -> None:
        self.front.append(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.append(self.front.pop())
        self.front.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) > len(self.back):
            self.back.insert(0, self.front.pop())
        return self.front.pop()

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            return self.front.pop()
        return self.back.pop(0)

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.back) > len(self.front):
            self.front.append(self.back.pop())
        return self.back.pop()

    def _balance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.insert(0, self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.pop())