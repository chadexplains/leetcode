class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = collections.defaultdict(list)
        for i in range(len(pid)):
            tree[ppid[i]].append(pid[i])
        res = []
        stack = [kill]
        while stack:
            node = stack.pop()
            res.append(node)
            stack.extend(tree[node])
        return res