nums = list(map(int, input().split()))

tracker = nums[0]
k = max(nums)
count = 1
for i in range(len(nums)):
    if nums[i] == tracker and count != 1:
        nums[i] = k
        count += 1
    elif nums[i] == tracker and count == 1:
        count += 1
    else:
        tracker = nums[i]
        count = 2

nums = list(sorted(nums))
print(nums)