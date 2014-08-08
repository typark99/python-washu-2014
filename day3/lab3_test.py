import unittest
import lab3

class Lab3Test(unittest.TestCase):
  def setup(self):
    pass
    
  def test_shout(self):
    self.assertEqual("HI!!", lab3.shout("hi. "))
    self.assertEqual("HI!", lab3.shout("hi"))
    self.assertEqual("HI!!", lab3.shout("hi?"))
    self.assertEqual("HI, HOW ARE YOU!!", lab3.shout("Hi, how are you?"))
    
  def test_reverse(self):
    self.assertEqual("", lab3.reverse(3))
    self.assertEqual("woh", lab3.reverse("how"))
    
  def test_reversewords(self):
    self.assertEqual("", lab3.reversewords(3))
    #self.assertEqual("hi.", lab3.reversewords("hi!"))
    #self.assertEqual("HI, HOW ARE YOU!!", lab3.reversewords("Hi, how are you?"))
  	
    
if __name__ == '__main__':
  unittest.main()