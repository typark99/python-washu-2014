# for numbers divisible by 3, print "Fizz"
# for numbers divisible by 5, print "Buzz"
# for numbers divisible by 3 and 5, print "FizzBuzz"

def FizzBuzz(i):
 try:
	if i % 15 == 0:
		raise Exception, "Divisible by 3 and 5!"	
	if i % 3 == 0:
		return "Fizz"
	if i % 5 == 0:
		return "Buzz"
 except:
 	if i % 15 == 0:
 		return "FizzBuzz"
# finally:
# 	print "Finally"
 return str(i)
 

for i in range(35):
	print str(i) + ":" + FizzBuzz(i)