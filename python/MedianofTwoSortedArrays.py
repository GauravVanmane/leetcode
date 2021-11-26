def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    pa = 0
    pb = 0
    result = []

    while pa < len(nums1) and pb < len(nums2):
        if nums1[pa] <= nums2[pb]:
            result.append(nums1[pa])
            pa += 1
        else:
            result.append(nums2[pb])
            pb += 1

    remained = nums1[pa:] + nums2[pb:]
    result.extend(remained)
    print(result)
    n = len(result)
    median = 0.00000
    if n % 2 :
        median = float(result[n//2])
        return median
    else:
        median = float(result[n // 2] + result[(n // 2) - 1])
        return median / 2