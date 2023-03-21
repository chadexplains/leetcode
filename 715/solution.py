class RangeModule:
    
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_range = [left, right]
        i, j = 0, len(self.ranges)
        while i < j:
            if self.ranges[i][1] < new_range[0]:
                i += 1
            elif self.ranges[i][0] > new_range[1]:
                break
            else:
                new_range[0] = min(new_range[0], self.ranges[i][0])
                new_range[1] = max(new_range[1], self.ranges[i][1])
                self.ranges.pop(i)
                j -= 1
        self.ranges.insert(i, new_range)

    def removeRange(self, left: int, right: int) -> None:
        i, j = 0, len(self.ranges)
        while i < j:
            if self.ranges[i][1] <= left:
                i += 1
            elif self.ranges[i][0] >= right:
                break
            else:
                if self.ranges[i][0] < left:
                    self.ranges.insert(i, [self.ranges[i][0], left])
                    i += 1
                if self.ranges[i][1] > right:
                    self.ranges.insert(i+1, [right, self.ranges[i][1]])
                    i += 2
                self.ranges.pop(i)
                j -= 1

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect_left(self.ranges, [left, float('-inf')])
        if i == len(self.ranges):
            return False
        return self.ranges[i][0] <= left and self.ranges[i][1] >= right
