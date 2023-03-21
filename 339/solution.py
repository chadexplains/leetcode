class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total_sum = 0
            for element in nestedList:
                if element.isInteger():
                    total_sum += element.getInteger() * depth
                else:
                    total_sum += dfs(element.getList(), depth + 1)
            return total_sum
        return dfs(nestedList, 1)