class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_milestones = max(milestones)
        total_milestones = sum(milestones)
        if max_milestones <= (total_milestones - max_milestones):
            return total_milestones
        else:
            return 2 * (total_milestones - max_milestones) + 1 if total_milestones % 2 == 1 else 2 * (total_milestones - max_milestones)