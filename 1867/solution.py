class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = [a, b, c]
        score = 0
        while len([p for p in piles if p > 0]) > 1:
            piles.sort(reverse=True)
            piles[0] -= 1
            piles[1] -= 1
            score += 1
        return score