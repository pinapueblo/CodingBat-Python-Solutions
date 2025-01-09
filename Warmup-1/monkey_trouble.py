def monkey_trouble(a_smile, b_smile):
  if(not a_smile and b_smile):
    return False
  if(a_smile and not b_smile):
    return False
  return True
