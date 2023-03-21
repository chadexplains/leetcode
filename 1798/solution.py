class Solution:
    def maxCoins(self, coins: List[int], k: int) -> int:
        remainders = [0] * k
        for coin in coins:
            remainders[coin % k] += 1
        result = min(remainders[0], 1)
        for i in range(1, k//2+1):
            if i != k-i:
                result += max(remainders[i], remainders[k-i])
            else:
                result += min(remainders[i], 1)
        return result