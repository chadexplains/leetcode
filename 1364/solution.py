class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee
        importance = 0
        queue = [id]
        while queue:
            curr_id = queue.pop(0)
            curr_employee = employee_dict[curr_id]
            importance += curr_employee.importance
            for subordinate_id in curr_employee.subordinates:
                queue.append(subordinate_id)
        return importance