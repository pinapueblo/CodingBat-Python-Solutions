def max_end3(nums):
  big = max(nums[0], nums[2])
  for i in range(len(nums)):
    nums[i] = big
  return nums
