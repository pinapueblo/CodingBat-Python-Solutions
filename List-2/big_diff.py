def big_diff(nums):
  big = nums[0]
  small = nums[0]
  for i in range(len(nums)):
    big = max(big, nums[i])
    small = min(small, nums[i])
  return big-small
