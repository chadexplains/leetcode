class Solution:
    def backtrack(self, foods, target):
        if target == [0, 0, 0]:
            return True
        if not foods or min(target) < 0:
            return False
        for i, (calories, *nutrients) in enumerate(foods):
            if self.backtrack(foods[i+1:], [t-calories for t, *n in zip(target, nutrients)]):
                return True
        return False
    def canEat(self, foods: List[List[int]], target: List[int]) -> bool:
        return self.backtrack(foods, target)