def singleNumber(self, nums: List[int]) -> int:
    num = set()
    for n in nums:
        if n not in num:
            #adding the element in the set
            num.add(n)
        else:
            #removing the duplicate element
            num.remove(n)
    return list(num)[0]
