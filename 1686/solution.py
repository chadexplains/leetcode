class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        stones = [(aliceValues[i] + bobValues[i], aliceValues[i], i) for i in range(n)]
        stones.sort(reverse=True)
        alice_score = 0
        bob_score = 0
        for i in range(n):
            if i % 2 == 0:
                alice_score += stones[i][1]
            else:
                bob_score += bobValues[stones[i][2]]
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return 0
        else:
            return -1