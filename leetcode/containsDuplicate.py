# Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if 
# every element is distinct.


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    freq = {}
    for num in nums:
        if not num in freq:
            freq[num] = 1
        else:
            return True
    return False