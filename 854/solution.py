class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        visited = set()
        queue = collections.deque([(A, 0)])
        while queue:
            curr, swaps = queue.popleft()
            if curr == B:
                return swaps
            for next_str in self.generate_next_strings(curr, B):
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append((next_str, swaps + 1))
        return -1
    
    def generate_next_strings(self, curr: str, target: str) -> List[str]:
        next_strings = []
        i = 0
        while curr[i] == target[i]:
            i += 1
        for j in range(i + 1, len(curr)):
            if curr[j] == target[i] and curr[j] != target[j]:
                next_str = curr[:i] + curr[j] + curr[i+1:j] + curr[i] + curr[j+1:]
                next_strings.append(next_str)
        return next_strings