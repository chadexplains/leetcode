class Solution:
    def averageWaitingTime(self, customers: List[List[int]], duration: int) -> float:
        total_wait_time = 0
        current_time = customers[0][0]
        for i in range(len(customers)):
            customer = customers[i]
            wait_time = max(0, current_time - customer[0])
            total_wait_time += wait_time + duration
            current_time = max(current_time, customer[0]) + duration
        return total_wait_time / len(customers)