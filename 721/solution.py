class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = {}
        uf = UnionFind(len(accounts))
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        root_to_emails = {}
        for i in range(len(accounts)):
            root = uf.find(i)
            if root not in root_to_emails:
                root_to_emails[root] = set()
            for email in accounts[i][1:]:
                root_to_emails[root].add(email)
        res = []
        for root, emails in root_to_emails.items():
            res.append([accounts[root][0]] + sorted(emails))
        return res