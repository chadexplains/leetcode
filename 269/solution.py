class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
                if j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2):
                    return ""
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        res = ""
        while queue:
            curr = queue.popleft()
            res += curr
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == len(in_degree) else ""