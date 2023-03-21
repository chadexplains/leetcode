class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        n = len(org)
        indegree = {i: 0 for i in org}
        adj_list = {i: [] for i in org}
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in indegree:
                    return False
                if i == 0:
                    continue
                if seq[i] not in adj_list[seq[i-1]]:
                    adj_list[seq[i-1]].append(seq[i])
                    indegree[seq[i]] += 1
        queue = [i for i in org if indegree[i] == 0]
        for i in range(n):
            if len(queue) != 1:
                return False
            node = queue.pop(0)
            if org[i] != node:
                return False
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return True