class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        max_left = partition_max = A[0]
        partition_index = 0
        for i in range(1, len(A)):
            if A[i] < max_left:
                partition_max = max(partition_max, max_left)
                partition_index = i
                max_left = partition_max
            else:
                max_left = max(max_left, A[i])
        return partition_index + 1