class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        nums = []
        subset_sums = set(sums)
        total_sum = sum(range(n + 1))
        while len(nums) < n:
            for num in range(total_sum + 1):
                if num in subset_sums:
                    subset_sums.remove(num)
                    nums.append(num - sum(nums))
                    break
        return nums