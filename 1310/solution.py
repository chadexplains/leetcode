def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    n = len(arr)
    prefix_xor = [0] * (n+1)
    for i in range(1, n+1):
        prefix_xor[i] = prefix_xor[i-1] ^ arr[i-1]
    output = []
    for query in queries:
        left, right = query
        output.append(prefix_xor[right+1] ^ prefix_xor[left])
    return output