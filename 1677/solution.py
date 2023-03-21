class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = [0] * 60
        pairs = 0
        for t in time:
            remainder = t % 60
            pairs += freq[(60 - remainder) % 60]
            freq[remainder] += 1
        return pairs