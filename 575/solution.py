class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = len(set(candyType))
        half_candies = len(candyType) // 2
        return min(unique_candies, half_candies)