class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        if len(words1) != len(words2):
            return False
        parent = {}
        for w1, w2 in pairs:
            if w1 not in parent:
                parent[w1] = w1
            if w2 not in parent:
                parent[w2] = w2
            parent[find(w1)] = find(w2)
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w1 not in parent or w2 not in parent or find(w1) != find(w2):
                return False
        return True