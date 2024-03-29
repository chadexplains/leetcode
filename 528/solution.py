class Solution:
    
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sum)
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left