def findDuplicate(self, nums: List[int]) -> int:
    i = nums[0]
    j = nums[0]
    flag = True
    while flag or i!= j:
        i = nums[i]
        j = nums[nums[j]]
        flag = False
    
    j = nums[0]
    while i != j:
        i = nums[i]
        j = nums[j]
    
    return i