def love6(a, b):
  sum = a+b
  difference = abs(a-b)
  if(a == 6 or b==6):
    return True
  if(sum == 6 or difference == 6):
    return True
  return False
