class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total_sum = sum(A)
        if total_sum % 3 != 0:
            return False
        one_third = total_sum // 3
        left, right = 0, len(A) - 1
        left_sum, right_sum = A[left], A[right]
        while left < right:
            if left_sum == one_third and right_sum == one_third:
                return True
            if left_sum != one_third:
                left += 1
                left_sum += A[left]
            if right_sum != one_third:
                right -= 1
                right_sum += A[right]
        return False