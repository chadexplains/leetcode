class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        count = [0] * batchSize
        for g in groups:
            count[g % batchSize] += 1
        ans = count[0]
        for i in range(1, (batchSize + 1) // 2):
            j = batchSize - i
            ans += min(count[i], count[j])
        if batchSize % 2 == 0:
            ans += count[batchSize // 2] // 2
        return ans