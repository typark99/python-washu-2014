class Burger():
  # Instance
  def __init__(self, filling, doneness, size, toppings, container):
    self.filling=filling # It can be self.meat=filling 
    self.doneness=doneness
    self.size=size
    if self.toppings_allowed(toppings):
       self.toppings = toppings
    else:
       self.toppings = []
    self.container=container
    
  def __str__(self):
    return "I'm a %s %s burger % (self.doneness, self.filling)"
    
  def toppings_allowed(self, attempted_toppings):
    allowed_toppings = ["cheese", "tomato", "lettuce", "bacon"]
    for topping in attempted_toppings:
      if topping not in allowed_toppings:
         return False
    return True
   
  # Behavior 
  def tastiness(self): 
     if "cheese" in self.toppings:
      return "very good!"
     #if self.toppings == "cheese"  # if cheese is the only option
     #  return "very good!"
     elif self.doneness == "raw":
       return "yuck!"
     else:
       return "meh"
      
  def cooking_time(self):
    # example sizes: 0.25, 0.33, 0.5
    # example doneness orders: raw, rare, medium, well done
    if self.doneness == "raw":
       time_for_doneness = 0
    elif self.doneness == "rare":
       time_for_doneness = 5
    elif self.doneness == "medium":
       time_for_doneness = 6
    elif self.doneness == "well done":
       time_for_doneness == 8
    else:
       return "UNKOWN"
    
    return self.size * 4 * time_for_doneness
    
#class VeggieBurger(Burger):
#   sef __init__(self, size, toppings, container):
#      self.filling = "veggie patty"
#      self.doneness="medium"
#      self.container=container
      
    
rare_burger = Burger("beef", "rare", 0.25, "cheese", "bread")
print rare_burger.cooking_time() # This is the same as cooking.time(rare_burger)

well_done_burger = Burger("beef", "well done", 0.33, "cheese", "bread")
print well_done_burger.__str__()
print well_done_burger.cooking_time()
print well_done_burger.tastiness()
#print well_done_burger.topping_allowed("onions")
       