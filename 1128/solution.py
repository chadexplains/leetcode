class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = {}
        count = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            if key in pairs:
                count += pairs[key]
                pairs[key] += 1
            else:
                pairs[key] = 1
        return count