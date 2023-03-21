class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
        energy = 0
        for task in tasks:
            energy += task[0]
            if energy < task[1]:
                energy = task[1]
        return energy