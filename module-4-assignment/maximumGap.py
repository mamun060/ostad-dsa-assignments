def maximumGap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    mapGap = int(0)
    for i in range(1, len(nums)):
        mapGap = max(mapGap, nums[i] - nums[i-1])
    return mapGap

arr = [0]
maxGap = maximumGap(arr)
print(maxGap)
