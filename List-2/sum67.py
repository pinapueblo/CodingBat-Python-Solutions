def sum67(nums):
  total = 0
  in_ignore_section = False
  for num in nums:
    if num == 6:
      in_ignore_section = True
    elif num == 7 and in_ignore_section:
      in_ignore_section = False
    elif not in_ignore_section:
      total += num
  return total
