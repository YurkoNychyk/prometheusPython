#Lesson05: Superfibonacci
def super_fibonacci(n,m):
	fib = 0
	if n <= m:
		return 1
	elif n > m:
		i = 0
		while i < m:
			fib = fib + super_fibonacci(n-i-1,m)
			i+=1
		return fib
		