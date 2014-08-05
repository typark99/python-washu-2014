class Clock():
  def __init__(self, hours, minutes=0):
    self.hours=hours
    self.minutes=minutes
    
  @classmethod
  def at(cls, hours, minutes=0):
    return cls(hours, minutes)
    
    
def __add__(self, num):
   hour_time = self.hours
   minute_time = self.minutes
   if minute_time+num<60:  
      hour_time = hour_time
      minute_time = minute_time + num
   if minute_time+num>=60 and hour_time+((minute_time+num)/60)<24:
      hour_time = hour_time + ((minute_time+num)/60)
      minute_time = minute_time + num - (60*((minute_time+num)/60))
   if minute_time+num>=60 and hour_time+((minute_time+num)/60)>=24:
      hour_time = hour_time+((minute_time+num)/60) - 24
      minute_time = minute_time + num - (60*((minute_time+num)/60))
    
   self.hours = hour_time
   self.minutes = minute_time
   return self # This lets you use self.hours and self.minutes again below
    
def __str__(self):
    hour_time = self.hours
    minute_time = self.minutes
    
    string_hour = str(hour_time)
    string_minute = str(minute_time)
    
    if len(string_hour) == 1:
       string_hour = "0" + string_hour
    else: 
       string_hour = string_hour
    
    if len(string_minute) == 1:
       string_minute = "0" + string_minute
    else: 
       string_hour = string_hour
       
    return string_hour+string_minute 
    
Clock.at(8).__str__()


  
  

       


        
       