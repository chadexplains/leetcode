class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        freq = sorted(freq.items(), key=lambda x: x[1])
        while k > 0:
            k -= freq[0][1]
            if k >= 0:
                freq.pop(0)
        return len(freq)