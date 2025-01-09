def front_back(str):
  if(len(str)<2):
    return str
  if(len(str)==2):
    return str[len(str)-1:]+ str[0:1]
  else:
    mid = str[1:len(str)-1]
    return str[len(str)-1:] + mid + str[0:1]
