class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        results = []
        for query in queries:
            i = j = 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    results.append(False)
                    break
                else:
                    i += 1
            else:
                if j == len(pattern):
                    results.append(True)
                else:
                    results.append(False)
        return results