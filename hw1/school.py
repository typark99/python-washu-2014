########################
# HW 1 -- Taeyong Park #
########################

class School:
 	def __init__(self, school):
  		self.school = school
  		self.db = {}  # Create self.db as a set.
 
 	def add(self, student, grade): # Define the add method. 
  		if grade in self.db:   
			self.db[grade].add(student) # Add a student name to the corresponding grade in the existing .db set.
   		else:
			self.db[grade] = {student} # If grade not in self.db, create a new set of student and grade.
   			
   	def grade(self, key): # Define the grade method
  		return self.db.get(key, None) # .get() returns a value for the given key. None is default.

	def sort(self): # Define the sort method
		sorted_students={} # Since the output should be a set, create an empty set.
		for key in self.db.keys(): # The method .keys() returns keys of the given set.
			sorted_students[key] = tuple(sorted(self.db[key])) # For every key in the .db set, it matches key(grade) and value(student).
		return sorted_students           # By using sorted(), sort the student names for each grade. And use tuple() to convert a set to a tuple.  
                                                       


