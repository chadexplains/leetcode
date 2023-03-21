class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        subsets = [[]]
        for num, count in freq.items():
            new_subsets = []
            for subset in subsets:
                for i in range(count + 1):
                    new_subsets.append(subset + [num] * i)
            subsets = new_subsets
        good_subsets = set()
        for subset in subsets:
            if len(subset) > 1 and any(subset.count(num) > 1 for num in set(subset)):
                product = 1
                for num in set(subset):
                    if subset.count(num) > 1:
                        product *= primes[num - 1]
                if product <= 30:
                    good_subsets.add(tuple(sorted(subset)))
        return len(good_subsets)