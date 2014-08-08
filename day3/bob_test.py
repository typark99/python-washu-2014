import unittest
import bob

class BobTest(unittest.TestCase):
  def setup(self):
    pass
    
  def test_first(self):
    self.assertEqual("Sure", bob.bob("What is wrong with you?"))
    
  def test_second(self):
    self.assertEqual("Fine. Be that way.", bob.bob("Bob?"))
    
  def test_third(self):
    self.assertEqual("Fine. Be that way.", bob.bob("Bob"))
    
if __name__ == '__main__':
  unittest.main()