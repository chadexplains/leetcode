class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        total = 0
        for num in nums:
            divisors = [1, num]
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    divisors.append(i)
                    if i != num // i:
                        divisors.append(num // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                total += sum(divisors)
        return total