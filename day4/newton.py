def sqr(number, guess):
	return = guess - ((guess**2 - number) / (2*guess))
	
	
sqr(579, 25)
number_to

def find_sqr(number, number, desired_precision=0.001, max_steps):
	guess = float(guess)
	number = float(number)
	steps = 0
	current_precision = 1
	while (current_precision < desired_precision) and (steps < max_steps):
		new_guess = sqr(number, guess)
		current_precision = abs(new_guess - guess)
		print "Step {0}: Current guess is {1} and precision is {2}".format(
			steps, new_guess, current_precision
		)
		guess = new_guess
		steps +=1
		return guess