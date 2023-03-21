class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        task_indices = list(range(n))
        task_indices.sort(key=lambda i: tasks[i][0])
        time = 0
        task_index = 0
        available_tasks = []
        result = []
        while task_index < n or available_tasks:
            if not available_tasks:
                time = tasks[task_indices[task_index]][0]
            while task_index < n and tasks[task_indices[task_index]][0] <= time:
                heapq.heappush(available_tasks, (tasks[task_indices[task_index]][1], task_indices[task_index]))
                task_index += 1
            if available_tasks:
                processing_time, index = heapq.heappop(available_tasks)
                result.append(index)
                time += processing_time
        return result