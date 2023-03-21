class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def can_eat_all(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= H
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if can_eat_all(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l