class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left, right = min(sweetness), sum(sweetness)
        while left < right:
            mid = (left + right + 1) // 2
            cur_sum, cuts = 0, 0
            for s in sweetness:
                cur_sum += s
                if cur_sum >= mid:
                    cur_sum = 0
                    cuts += 1
            if cuts >= K + 1:
                left = mid
            else:
                right = mid - 1
        return left