class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            numBottles, rem = divmod(numBottles, numExchange)
            total += numBottles
            numBottles += rem
        return total