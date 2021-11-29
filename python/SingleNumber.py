def singleNumber(self, nums: List[int]) -> int:
    num = set()
    for n in nums:
        if n not in num:
            num.add(n)
        else:
            num.remove(n)
    return list(num)[0]