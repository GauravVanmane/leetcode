def searchInsert(self, nums: List[int], target: int) -> int:
    if nums[-1] >= target:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            elif nums[i] == target:
                return i
    else:
        return len(nums)