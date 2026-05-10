Class TokenBudget:
 def_init__(self, daily_limit : int)
   self.daily_limit = daily_limit
   self.used_today = 0 
#i am not sure if  i can use that without initializing in def_init function

  def_can_spend(self,tokens:init) - > bool
   return self_used_today + tokens <= daily_limit

   #i am not sure above is right or not as i am not able to catch the initialization part
    




