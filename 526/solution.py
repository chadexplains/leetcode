class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.used = [False] * (n + 1)
        self.backtrack(1, [])
        return self.count
    
    def backtrack(self, index, perm):
        if index > len(self.used) - 1:
            self.count += 1
            return
        for i in range(1, len(self.used)):
            if not self.used[i] and (i % index == 0 or index % i == 0):
                self.used[i] = True
                perm.append(i)
                self.backtrack(index + 1, perm)
                perm.pop()
                self.used[i] = False
