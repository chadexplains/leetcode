class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = collections.defaultdict(int)
        res = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            if complement in freq:
                res += freq[complement]
            freq[remainder] += 1
        return res