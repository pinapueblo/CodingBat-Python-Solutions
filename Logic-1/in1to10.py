def in1to10(n, outside_mode):
  if(n>=1 and n<=10 and not outside_mode):
    return True
  if((n<=1 or n>=10) and outside_mode):
    return True
  return False
    
  
