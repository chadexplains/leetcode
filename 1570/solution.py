class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzeros[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        for i, num in self.nonzeros.items():
            if i in vec.nonzeros:
                sum += num * vec.nonzeros[i]
        return sum