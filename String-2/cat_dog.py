def cat_dog(str):
  dogCount = 0
  catCount = 0
  for i in range(len(str)):
    if(str[i:i+3] == 'cat'):
      catCount+=1
    if(str[i:i+3] == 'dog'):
      dogCount+=1
  
  if(dogCount==catCount):
    return True
  return False
