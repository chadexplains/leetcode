class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        candies_given = 0
        round_num = 1
        while candies_given < candies:
            for i in range(num_people):
                candies_to_give = candies_given + i + 1 + (round_num - 1) * num_people
                if candies_given + candies_to_give <= candies:
                    ans[i] += candies_to_give
                    candies_given += candies_to_give
                else:
                    ans[i] += candies - candies_given
                    candies_given = candies
                    break
            round_num += 1
        return ans