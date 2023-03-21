```class Solution:
    def check_arithmetic(self, arr):
        if len(arr) <= 2:
            return True
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
    
    def solve(self, nums, queries):
        ans = []
        for l, r in queries:
            subarrays = [nums[i:j+1] for i in range(l, r+1) for j in range(i, r+1) if (j-i+1) % 2 != 0]
            subarrays = [subarray for subarray in subarrays if self.check_arithmetic(subarray)]
            ans.append(len(subarrays))
        return ans```