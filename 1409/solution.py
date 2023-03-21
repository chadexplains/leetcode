def processQueries(queries: List[int], m: int) -> List[int]:
    result = []
    permutation = list(range(1, m+1))
    for query in queries:
        index = permutation.index(query)
        result.append(index)
        permutation.pop(index)
        permutation.insert(0, query)
    return result