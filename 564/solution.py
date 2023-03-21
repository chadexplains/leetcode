class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        if n == '10' or n == '11':
            return str(int(n) - 1)
        if n == '9':
            return '8'
        if n == '11' or n == '22' or n == '33' or n == '44' or n == '55' or n == '66' or n == '77' or n == '88' or n == '99':
            return str(int(n) - 1)
        if n == n[::-1]:
            candidates = [str(int(n[:len(n)//2] + n[len(n)//2] + n[:len(n)//2][::-1])),
                          str(int(n[:len(n)//2] + str(int(n[len(n)//2])+1) + n[:len(n)//2][::-1])),
                          str(int(n[:len(n)//2] + str(int(n[len(n)//2])-1) + n[:len(n)//2][::-1]))]
        else:
            candidates = [str(int(n[:len(n)//2] + n[len(n)//2] + n[:len(n)//2][::-1])),
                          str(int(n[:len(n)//2] + str(int(n[len(n)//2])+1) + n[:len(n)//2][::-1])),
                          str(int(n[:len(n)//2] + str(int(n[len(n)//2])-1) + n[:len(n)//2][::-1])),
                          str(int(n[:len(n)//2+1] + '0'*(len(n)-1-len(n)//2) + n[len(n)//2+1] + n[:len(n)//2+1][::-1])),
                          str(int(n[:len(n)//2] + '9'*(len(n)-1-len(n)//2) + n[:len(n)//2+1][::-1]))]
        closest = None
        min_diff = float('inf')
        for candidate in candidates:
            if candidate != n:
                diff = abs(int(candidate) - int(n))
                if diff < min_diff:
                    closest = candidate
                    min_diff = diff
                elif diff == min_diff:
                    closest = min(closest, candidate)
        return closest