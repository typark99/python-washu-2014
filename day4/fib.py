def fib(n):
	if n<=1:
		return n
	return fib(n-1)+fib(n-2)
	
for i in range(10):
	print "{0} : {1}".format(i, fib(i))