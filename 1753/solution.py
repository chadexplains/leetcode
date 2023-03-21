class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        piles = [a, b, c]
        piles.sort(reverse=True)
        score = 0
        while piles[1] > 0:
            piles[0] -= 1
            piles[1] -= 1
            score += 1
            piles.sort(reverse=True)
        if piles[0] > 0 and piles[1] > 0:
            piles[0] -= 1
            piles[1] -= 1
            score += 1
        return score