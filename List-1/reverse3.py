def reverse3(nums):
  result=3*[0]
  for i in range(len(nums)):
    result[i] = nums[len(nums)-1-i]
  return result
