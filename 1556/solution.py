def minInteger(num: str, k: int) -> str:
    occurrences = [[] for _ in range(10)]
    for i, digit in enumerate(num):
        occurrences[int(digit)].append(i)
    result = []
    seg_tree = SegmentTree(len(num))
    for _ in range(len(num)):
        for digit in range(10):
            if occurrences[digit]:
                i = occurrences[digit][0]
                swaps = seg_tree.query(i)
                if i - swaps <= k:
                    result.append(str(digit))
                    occurrences[digit].pop(0)
                    k -= i - swaps
                    seg_tree.update(i)
                    break
        else:
            break
    return ''.join(result)

class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.n = n

    def update(self, i):
        self._update(0, 0, self.n - 1, i)

    def _update(self, node, start, end, i):
        if start == end:
            self.tree[node] = 1
        else:
            mid = (start + end) // 2
            if i <= mid:
                self._update(2 * node + 1, start, mid, i)
            else:
                self._update(2 * node + 2, mid + 1, end, i)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, i):
        return self._query(0, 0, self.n - 1, i)

    def _query(self, node, start, end, i):
        if start == end:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            if i <= mid:
                return self.tree[node] - self._query(2 * node + 2, mid + 1, end, i) - self.lazy[node]
            else:
                return self._query(2 * node + 1, start, mid, i) - self.lazy[node]

            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
