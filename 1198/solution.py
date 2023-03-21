```python
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for val in mat[0]:
            present_in_all_rows = True
            for row in mat[1:]:
                if bisect_left(row, val) == len(row) or row[bisect_left(row, val)] != val:
                    present_in_all_rows = False
                    break
            if present_in_all_rows:
                return val
        return -1
```