class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        hash_table = {0:1}
        for num in nums:
            sum += num
            if sum - k in hash_table:
                count += hash_table[sum - k]
            if sum in hash_table:
                hash_table[sum] += 1
            else:
                hash_table[sum] = 1
        return count