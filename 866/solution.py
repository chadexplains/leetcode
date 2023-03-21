class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        def is_palindrome(n):
            return str(n) == str(n)[::-1]
        
        if N <= 2:
            return 2
        
        if N == 3:
            return 3
        
        if N <= 5:
            return 5
        
        if N <= 7:
            return 7
        
        if N <= 11:
            return 11
        
        for i in range(10**len(str(N//2)), 10**5):
            if is_palindrome(i):
                if i >= N and is_prime(i):
                    return i
