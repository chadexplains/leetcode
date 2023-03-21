class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(source):
            indices[c].append(i)
        subseqs = 0
        curr_idx = -1
        for c in target:
            if c not in indices:
                return -1
            possible_indices = indices[c]
            idx = bisect_right(possible_indices, curr_idx)
            if idx == len(possible_indices):
                subseqs += 1
                curr_idx = possible_indices[0]
            else:
                curr_idx = possible_indices[idx]
        return subseqs + 1