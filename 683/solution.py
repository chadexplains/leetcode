class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        n = len(bulbs)
        days = [0] * n
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
            left, right = position - K - 2, position + K
            if 0 <= left < n and days[left] == day - K - 1 and days[left+1:position-1] == [0] * (position - left - 2):
                return day
            if right < n and days[right] == day - K - 1 and days[position:right] == [0] * (right - position):
                return day
        return -1