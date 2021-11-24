class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = dict()
        for i in range(0,len(nums)):
            dicto[nums[i]]=i
            
        for i in range(0,len(nums)):
            ToCheck =  target - nums[i]
            if dicto.get(ToCheck) and dicto.get(ToCheck)!=i:
                return sorted([dicto[ToCheck],i])
