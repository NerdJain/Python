#Prime/Not Prime (Abhishek - 16CSU015)

def main():
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

if __name__ == '__main__':
	main()

#Output:
#C:\Users\DELL\py4e>python prime.py
#Enter a number: 5
#Prime number

#Enter a number: 67
#Prime number

#Enter a number: 81
#Not a prime number

#Enter a number: 91
#Not a prime number