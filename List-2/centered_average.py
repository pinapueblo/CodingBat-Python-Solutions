def centered_average(nums):
  ordered = sorted(nums)
  trimmed = ordered[1:-1]
  total = sum(trimmed)
  avg = total//len(trimmed)
  return avg
  
