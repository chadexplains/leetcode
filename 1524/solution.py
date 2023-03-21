class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        odd_freq = even_freq = 1
        freq = {0: 1}
        res = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                res += odd_freq
                even_freq += 1
            else:
                res += even_freq
                odd_freq += 1
            freq[prefix_sum % 2] = freq.get(prefix_sum % 2, 0) + 1
        return res