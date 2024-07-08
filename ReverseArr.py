def reverseNum(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums

nums = [4, 5, 6, 7, 8]
print("Reversed Array is:", reverseNum(nums))
