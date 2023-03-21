class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = re.sub('[^0-9]', ' ', word)
        nums = [int(num.lstrip('0')) for num in word.split()]
        return len(set(nums))