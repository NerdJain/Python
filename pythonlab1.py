#Prime
	num = int(input("Enter a number: "))
	c = 0
	d = int(num/2)
	if num > 1:
		for i in range(1,d+1):
			if num % i == 0:
				c += 1	
		if c >= 2:
			print("Not a prime number")
		else:
			print("Prime number")
	else:
		print("Not a prime number")

#Factorial
def fact(num):
	if num < 2:
		return 1
	f = num * fact(num-1)
	return f

num = int(input("Enter a number: "))
result = fact(num)
print(f"Factorial of {num}: {result}")

#Fibonacci
	n = int(input("Enter length of series: "))
	a = 0
	b = 1
	c = -1
	print(a)
	print(b)
	for i in range(0,n-2):
		c = a+b
		a = b
		b = c
		print(b)
