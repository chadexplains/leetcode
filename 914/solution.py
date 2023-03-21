class Solution:
    def hasGroupsSizeX(self, deck: List[int], k: int) -> bool:
        count = collections.Counter(deck)
        gcd = count[deck[0]]
        for val in count.values():
            gcd = math.gcd(gcd, val)
        return gcd >= k