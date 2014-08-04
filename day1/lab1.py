def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  
  numbers = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  
  for i in numbers: 
   if num>=(2**i):
      digits.append('1')
      num = num - (2**i)
  #   print num
  #   print digits
   else:
      digits.append('0')
      
  print ''.join(digits)
  
binarify(130)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0 
  return result 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result
   