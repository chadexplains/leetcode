class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_milestone = max(milestones)
        sum_milestones = sum(milestones)
        sum_other_milestones = sum_milestones - max_milestone
        if max_milestone <= sum_other_milestones:
            return sum_milestones
        else:
            return 2 * sum_other_milestones + 1