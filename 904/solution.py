class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = 0
        right = 0
        max_length = 0
        fruit_counts = {}
        while right < len(tree):
            fruit_counts[tree[right]] = fruit_counts.get(tree[right], 0) + 1
            while len(fruit_counts) > 2:
                fruit_counts[tree[left]] -= 1
                if fruit_counts[tree[left]] == 0:
                    del fruit_counts[tree[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length