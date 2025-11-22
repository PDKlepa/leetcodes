
def singleNumber(nums):
    prev, next = None, None
    nums.sort()
    while len(nums) > 1:
        prev = nums[0]
        next = nums[1]
        if prev != next:
            return prev
        else:
            nums.pop(0)
            nums.pop(0)
    return nums[0]


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))