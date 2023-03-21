class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers_of_three = {1}
        while powers_of_three[-1] < n:
            powers_of_three.add(powers_of_three[-1] * 3)
        def backtrack(curr_sum, curr_power):
            if curr_sum == n:
                return True
            if curr_sum > n or curr_power > powers_of_three[-1]:
                return False
            for power in powers_of_three:
                if power not in powers_of_three:
                    continue
                powers_of_three.remove(power)
                if backtrack(curr_sum + power, power * 3):
                    return True
                powers_of_three.add(power)
            return False
        return backtrack(0, 1)