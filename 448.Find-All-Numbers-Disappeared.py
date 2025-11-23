
def findDisappearedNumbers(nums):
    present = set(nums)
    result = []
    for i in range(1, len(nums)+1):
        if i not in present:
            result.append(i)
    return result




print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))
print(findDisappearedNumbers([1,1,1]))
print(findDisappearedNumbers([1,2,2]))