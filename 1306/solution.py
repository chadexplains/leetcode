class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            if i + arr[i] < n and i + arr[i] not in visited:
                q.append(i + arr[i])
            if i - arr[i] >= 0 and i - arr[i] not in visited:
                q.append(i - arr[i])
            visited.add(i)
        return False