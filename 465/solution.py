class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = collections.defaultdict(int)
        for transaction in transactions:
            balances[transaction[0]] -= transaction[2]
            balances[transaction[1]] += transaction[2]
        debt = list(balances.values())
        return self.dfs(debt, 0)
    
    def dfs(self, debt, start):
        while start < len(debt) and debt[start] == 0:
            start += 1
        if start == len(debt):
            return 0
        res = float('inf')
        for i in range(start+1, len(debt)):
            if debt[i] * debt[start] < 0:
                debt[i] += debt[start]
                res = min(res, 1 + self.dfs(debt, start+1))
                debt[i] -= debt[start]
        return res