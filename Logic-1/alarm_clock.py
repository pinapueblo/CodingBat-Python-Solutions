def alarm_clock(day, vacation):
  if(vacation and (day>=1 and day<=5)):
    return "10:00"
  elif(vacation and (day==0 or day==6)):
    return "off"
  elif((day>=1 and day<=5)):
    return "7:00"
  return "10:00"
    
