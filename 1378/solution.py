class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrack(jobs, workloads, idx, max_time):
            if max_time >= self.res:
                return
            if idx == len(jobs):
                self.res = max_time
                return
            for i in range(len(workloads)):
                if workloads[i] + jobs[idx] <= max_time:
                    workloads[i] += jobs[idx]
                    backtrack(jobs, workloads, idx + 1, max(workloads))
                    workloads[i] -= jobs[idx]
                if workloads[i] == 0 or workloads[i] + jobs[idx] == max_time:
                    break
        self.res = float('inf')
        jobs.sort(reverse=True)
        backtrack(jobs, [0] * k, 0, 0)
        return self.res