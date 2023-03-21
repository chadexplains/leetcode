class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_val = float('inf')
        abs_val_sum = 0
        neg_count = 0
        for row in matrix:
            for val in row:
                abs_val = abs(val)
                if abs_val < min_abs_val:
                    min_abs_val = abs_val
                abs_val_sum += abs_val
                if val < 0:
                    neg_count += 1
        if neg_count % 2 == 0:
            return abs_val_sum
        else:
            return abs_val_sum - 2 * min_abs_val