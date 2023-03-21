class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        freq = {}
        for key in count:
            if count[key] in freq:
                return False
            freq[count[key]] = 1
        return True