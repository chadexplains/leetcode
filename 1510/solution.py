class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        last_two_odds = [0, 0]
        for num in arr:
            if num % 2 == 1:
                odd_count += 1
                if odd_count == 3:
                    return True
                last_two_odds[0], last_two_odds[1] = last_two_odds[1], num
            else:
                odd_count = 0
        return False