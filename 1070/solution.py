class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzeros[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, num in vec.nonzeros.items():
            if i in self.nonzeros:
                result += self.nonzeros[i] * num
        return result