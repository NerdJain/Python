import time

def main():
	start_time = time.time()
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

	exe_time = time.time() - start_time
	print(exe_time)
if __name__ == '__main__':
	main()


#Output:
#C:\Users\DELL\py4e>python fibonacci.py
#Enter length of series: 10
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34
