class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = collections.Counter(nums)
        values = [(k, v) for k, v in freq.items()]
        values.sort(key=lambda x: x[1], reverse=True)
        n, m = len(nums), len(quantity)
        dist = [set() for _ in range(m)]
        def backtrack(pos):
            if pos == n:
                return True
            for i in range(m):
                if quantity[i] > 0 and nums[pos] in values[:i+1] and nums[pos] not in dist[i]:
                    dist[i].add(nums[pos])
                    quantity[i] -= 1
                    if backtrack(pos+1):
                        return True
                    quantity[i] += 1
                    dist[i].remove(nums[pos])
            return False
        return backtrack(0)