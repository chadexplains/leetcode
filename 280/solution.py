def wiggleSort(nums):
    nums.sort()
    for i in range(1, len(nums)-1, 2):
        if nums[i] > nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums