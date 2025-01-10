def string_bits(str):
  result = ""
  for i in range(0,len(str),2):
    result+=str[i:i+1]
  return result
