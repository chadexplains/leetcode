def maximumRequests(n: int, requests: List[List[int]]) -> int:
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
                if balances[j] > 0:
                    transfer_amount = min(balances[j], -balances[i])
                    balances[i] += transfer_amount
                    balances[j] -= transfer_amount
                    total_transfers += transfer_amount
            else:
                j = transfers.index(-transfers[i])
                if balances[j] < 0:
                    transfer_amount = min(-balances[j], balances[i])
                    balances[i] -= transfer_amount
                    balances[j] += transfer_amount
                    total_transfers += transfer_amount
    return total_transfers