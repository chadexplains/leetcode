class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        ones = twos = 0
        for stone in stones:
            if stone % 3 == 1:
                ones += 1
            elif stone % 3 == 2:
                twos += 1
        if ones % 2 == 0 and twos % 2 == 0:
            return len(stones) % 2 == 0
        return abs(ones - twos) > 2 or len(stones) % 2 == 0