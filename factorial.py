
#Factorial (Abhishek - 16CSU015)
def fact(num):
	if num < 2:
		return 1
	f = num * fact(num-1)
	return f

def main():
	#start_time = time.time()
	num = int(input("Enter a number: "))
	result = fact(num)
	print(f"Factorial of {num}: {result}")
	#exe_time = time.time() - start_time
	#print(exe_time)

if __name__ == "__main__":
	main()


#Output:
#C:\Users\DELL\py4e>python factorial.py
#Enter a number: 5
#Factorial of 5: 120

#Enter a number: 7
#Factorial of 7: 5040

#Enter a number: 8
#Factorial of 8: 40320

#Enter a number: 4
#Factorial of 4: 24