class TwoSum:
    
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            diff = value - num
            if diff in self.nums:
                if diff == num and self.nums[num] > 1:
                    return True
                elif diff != num:
                    return True
        return False