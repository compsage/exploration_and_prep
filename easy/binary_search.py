import math

def binary_search(nums, target, mid=0) :
    
    print(nums, target, mid)
    p_mid = mid
    mid = math.floor(len(nums)/2)

    if len(nums) > 0 and target == nums[mid] :
        return p_mid+mid
    elif mid == 0 :
        return -1
    elif target < nums[mid] :
        return binary_search(nums[:mid], target, 0)
    elif target > nums[mid] :
        return binary_search(nums[mid:], target, p_mid+mid)

def binary_search2(nums, target, start, end) :
    mid = math.floor((start+end)/2)
    print(target, nums, start, mid, end)

    if nums and target == nums[mid] :
        return mid
    elif mid == 0 :
        return -1
    elif target < nums[mid] :
        return binary_search2(nums, target, start, mid)
    elif target > nums[mid] :
        return binary_search2(nums, target, mid, end)


nums = [2, 4, 6, 8, 10, 12, 14, 16]

target = 16

nums = [10, 12]
target = 11


#output should be 2
print(binary_search2(nums, target, 0, len(nums)))
