class Solution:
    def getXORSum(self, arr: List[int], b: List[int]) -> int:
        xor_sum = 0
        and_sum = 0
        for num in arr:
            xor_sum ^= num
        for i in range(len(arr)):
            and_sum += arr[i] & b[i]
        return xor_sum & and_sum