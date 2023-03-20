class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.row = 0
        self.col = 0
        self.v = v

    def next(self) -> int:
        val = self.v[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self) -> bool:
        while self.row < len(self.v) and not self.v[self.row]:
            self.row += 1
            self.col = 0
        return self.row < len(self.v)