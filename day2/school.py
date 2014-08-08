class School():
 def __init__(self, name):
  self.name=name
 
 @classmethod
 def school(cls, name="Haleakala Hippy School"):
  return cls(name)
  
 #def db(self, ):
 
 def add(self, student, grade):
  self.student = student
  self.grade = grade
  return "Add %s to grade %d." %(student, grade)
  
one = School("random school")
print one.school()
print one.add("Aimee", 2)