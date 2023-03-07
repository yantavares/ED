n, k = map(int, input().split())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
for l in range(len(nums)):
    if nums[l] < 0:
        temp = -nums[l]
        if nums[l] % 2 != 0:
            nums[l] = (nums[l], -(temp % k) - 0.5)
        else:
            nums[l] = (nums[l], -(temp % k))
    else:
        if nums[l] % 2 != 0:
            nums[l] = (nums[l], nums[l] % k - 0.5)
        else:
            nums[l] = (nums[l], nums[l] % k)

nums = sorted(nums, key=lambda nums: nums[0],)
nums = sorted(nums, key=lambda nums: nums[1], reverse=True)

print(nums)
# for n in nums:
#     print(n[0], end=" ")
