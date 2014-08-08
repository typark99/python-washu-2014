import unittest
import ordinal

class OrdinalTest(unittest.TestCase):
  def setup(self):
    pass
  
  def test_first(self):
    self.assertEqual("1st", ordinal.ordinal(1)) # first ordinal is document from importing
  
  def test_second(self):
    self.assertEqual("2nd", ordinal.ordinal(2))
  
  def test_third(self):
  	self.assertEqual("3rd", ordinal.ordinal(3))
  	
  def test_forth(self):
  	self.assertEqual("4th", ordinal.ordinal(4))
  	
  def test_eleventh(self):
  	self.assertEqual("11th", ordinal.ordinal(11))
  
  def test_string(self):
  	self.assertEqual("Improper input", "xy")
  
  if __name__ == '__main__':
    unittest.main()