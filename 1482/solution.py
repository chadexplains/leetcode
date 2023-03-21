class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            bouquets = flowers = 0
            for day in bloomDay:
                if day > mid:
                    flowers = 0
                else:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets == m:
                            break
            if bouquets == m:
                right = mid
            else:
                left = mid + 1
        return left