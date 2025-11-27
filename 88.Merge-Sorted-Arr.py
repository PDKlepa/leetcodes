

def merge(nums1, m, nums2, n):
    if m < 1:
        if n == 0:
            return nums1
        else:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
    else:
        for i in range(len(nums2)):
            nums1[len(nums1)-i-1] = nums2[i]


    nums1.sort()
    return(nums1)






print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([0,0,0], 0, [1,2,3], 1))