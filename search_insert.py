from bisect import bisect_left

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    pos = bisect_left(nums, target)
    print(pos)

searchInsert([1,3,5,6], 2)