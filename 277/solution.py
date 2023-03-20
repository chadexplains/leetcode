def findCelebrity(self, n: int) -> int:
        left, right = 0, n-1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for i in range(n):
            if i != left and (knows(left, i) or not knows(i, left)):
                return -1
        return left