def last2(str):
  count = 0
  for i in range(len(str)-2):
    if(str[i:i+2] == str[len(str)-2:]):
      count+=1
  return count
