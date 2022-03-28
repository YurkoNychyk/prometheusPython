#Lesson05: counter(a,b)
def counter(a,b):
	a = set(str(a))
	b = set(str(b))
	foundling = 0
	for digit_to_find in b:

		for checked_digit in a:
			print digit_to_find + " " + checked_digit
			if digit_to_find == checked_digit:
				foundling += 1
				print "Its a match!"
				exit


	return foundling			
	

