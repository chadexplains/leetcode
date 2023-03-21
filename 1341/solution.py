```python
from typing import List

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    row_counts = []
    for i, row in enumerate(mat):
        row_counts.append((i, sum(row)))
    row_counts.sort(key=lambda x: x[1])
    return [x[0] for x in row_counts[:k]]
```