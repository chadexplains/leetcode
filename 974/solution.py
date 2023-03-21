class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}
        for a in A:
            prefix_sum += a
            remainder = prefix_sum % K
            if remainder < 0:
                remainder += K
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        return count