class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {x:i for i,x in enumerate(row)}
        ans = 0
        for i in range(0,len(row),2):
            x = row[i]
            if row[i+1] != (x^1):
                y = x^1
                j = pos[y]
                row[i+1],row[j] = row[j],row[i+1]
                pos[row[j]] = j
                pos[row[i+1]] = i+1
                ans += 1
        return ans