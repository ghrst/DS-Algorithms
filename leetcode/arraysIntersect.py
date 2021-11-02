# Problem: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as 
# many times as it shows in both arrays and you may return the result in any order.


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    freq = {}
    for i in nums1:
        if not i in freq:
            freq[i] = [1, 0]
        else:
            freq[i][0] += 1
            
    for j in nums2:
        if j in freq:
            freq[j][1] += 1
            
    results = []
    for k, v in freq.items():
        if v[0] == v[1]:
            results.extend([k] * v[0])
        else:
            results.extend([k] * min(v))
            
    return results