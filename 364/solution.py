class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def get_depth(nestedList):
            if not nestedList:
                return 0
            depth = 1
            for item in nestedList:
                if not item.isInteger():
                    depth = max(depth, 1 + get_depth(item.getList()))
            return depth
        def get_sum(nestedList, depth):
            if not nestedList:
                return 0
            total = 0
            for item in nestedList:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += get_sum(item.getList(), depth - 1)
            return total
        max_depth = get_depth(nestedList)
        return get_sum(nestedList, max_depth)