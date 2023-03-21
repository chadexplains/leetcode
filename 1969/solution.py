class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        max_num = (1 << p) - 1
        num_operations = (max_num - 1) // 2
        return pow((max_num - 1), num_operations, 1000000007) * max_num % 1000000007