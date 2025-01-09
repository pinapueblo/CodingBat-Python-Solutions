def rotate_left3(nums):
  result = 3*[0]
  
  for i in range(len(nums)):
    result[i]=nums[i-2]
  return result
