class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = [(start, 0)]
        visited = set()
        while queue:
            gene, mutations = queue.pop(0)
            if gene == end:
                return mutations
            for i in range(len(gene)):
                for c in ['A', 'C', 'G', 'T']:
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations+1))
        return -1