class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        freq = defaultdict(int)
        for companies in favoriteCompanies:
            for company in companies:
                freq[company] += 1
        res = []
        for i, companies in enumerate(favoriteCompanies):
            is_subset = False
            for j, other_companies in enumerate(favoriteCompanies):
                if i != j and set(companies).issubset(set(other_companies)):
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)
        return res