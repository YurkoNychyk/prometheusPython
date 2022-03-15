#Lesson03 Factorial 
import sys
n=0
i=0
result=1

def text_prompt(msg):
	try:
		return raw_input(msg)
	except NameError:
		return input(msg)

n=int(text_prompt('Input N:'))

if n<0 :
	print ('N should not be less then zero')
else:
	for i in range (n):
		result = result * (i+1)
	print(str(n) + '! = ' + str(result))
