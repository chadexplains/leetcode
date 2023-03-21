class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.ptrs = [0, 0]
        self.flag = 0

    def next(self) -> int:
        if self.hasNext():
            val = self.vectors[self.flag][self.ptrs[self.flag]]
            self.ptrs[self.flag] += 1
            self.flag = (self.flag + 1) % 2
            return val

    def hasNext(self) -> bool:
        while self.ptrs[self.flag] == len(self.vectors[self.flag]) and self.ptrs[(self.flag + 1) % 2] < len(self.vectors[(self.flag + 1) % 2]):
            self.flag = (self.flag + 1) % 2
        return self.ptrs[self.flag] < len(self.vectors[self.flag])