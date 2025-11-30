

def nextGreaterElement(nums1, nums2):
    result = []
    for i in range(len(nums1)):
        curr = nums1[i]
        indexInNums2 = nums2.index(curr)
        greatest = -1
        for j in range(indexInNums2, len(nums2)-1):
            if nums2[j] > curr:
                greatest = nums2[j]
                break
        result.append(greatest)
        print(result)
    return(result)



nextGreaterElement([4,1,2], [1,3,4,2])
#print("-")
#nextGreaterElement([2,4], [1,2,3,4])
#nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])