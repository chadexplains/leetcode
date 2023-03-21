class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        balances = [0] * n
        transfers = [0] * n
        for request in requests:
            from_account, to_account, amount = request
            balances[from_account] -= amount
            balances[to_account] += amount
            transfers[from_account] -= 1
            transfers[to_account] += 1
        total_transfers = 0
        for i in range(n):
            while balances[i] == 0 and transfers[i] != 0:
                if transfers[i] > 0:
                    j = transfers.index(-transfers[i])
                    balances[i] += 1
                    balances[j] -= 1
                    transfers[i] -= 1
                    transfers[j] += 1
                    total_transfers += 1
                else:
                    j = transfers.index(-transfers[i])
                    balances[i] -= 1
                    balances[j] += 1
                    transfers[i] += 1
                    transfers[j] -= 1
                    total_transfers += 1
        return total_transfers