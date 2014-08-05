def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  
  numbers = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  
  for i in numbers: 
   if num>=(2**i):
      digits.append('1')
      num = num - (2**i)
   else:
      digits.append('0')
  return ''.join(digits)
  
#print binarify(130)

## From Dave
def binarify2(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits=[]
  while num>0:
    digits.append(num%2)
    num=num/2
  digits=digits[::-1]
  return ''.join(str(e) for e in digits)

#print binarify2(130)


def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  while num>0:
    digits.append(num%base)
    num=num/base
  digits=digits[::-1]
  return ''.join(str(e) for e in digits)
  
## From Dalston
def int_to_base2(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  for i in range(13, -1, -1):
  	power = base**i
  	digits.append(str(num/power))
  	num %= power
  return ''.join(digits)
  
#print int_to_base(13000,2)
#print int_to_base2(13000,2)
#print int_to_base(400,5)
#print int_to_base2(400,5)
#print int_to_base(48,4)
#print int_to_base2(48,4)
  

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0: return 0 
  result = 0
  for i in range(0, len(string)):
    power = range(0, len(string))
    power = power[::-1]
    result +=int(string[i])*base**power[i]
  return result
  
#print base_to_int("10001", 2)
#print base_to_int("1321", 4)
  
def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  tmp = base_to_int(str1, base1)+base_to_int(str2, base2)
  result = int_to_base(tmp, base1) # it will return a string in base base1
  return result 
  
#print flexibase_add("10001", "1321", 2, 4)

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  tmp = base_to_int(str1, base1)*base_to_int(str2, base2)
  result = int_to_base(tmp, base1)
  return result 
  
#print flexibase_multiply("10001", "1321", 2, 4)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result