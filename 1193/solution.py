class Solution:
    def getAccountBalance(self, transactions: List[List[str]]) -> str:
        balance = defaultdict(int)
        for transaction in transactions:
            balance[transaction[0]] -= int(transaction[2])
            balance[transaction[1]] += int(transaction[2])
        return json.dumps(balance)