class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = collections.Counter(deliciousness)
        max_sum = max(deliciousness) * 2
        count = 0
        for num in freq:
            for i in range(0, 22):
                power = 1 << i
                if power >= num * 2 and power - num in freq:
                    if power - num == num:
                        count += freq[num] * (freq[num] - 1) // 2
                    else:
                        count += freq[num] * freq[power - num]
        return count % (10 ** 9 + 7)