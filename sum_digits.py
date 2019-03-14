#Sum of digits (Abhishek - 16CSU015)
def main():

	num = int(input("Enter a number: "))
	sum = 0
	temp = num
	while(num > 0):
		digit = num % 10
		sum = sum + digit
		num = num//10

	print(f"Sum of digits of {temp} is: {sum}")

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python sum_digits.py
# Enter a number: 45
# Sum of digits of 45 is: 9
#--------------------------------
# Enter a number: 4554
# Sum of digits of 4554 is: 18
#--------------------------------
# Enter a number: 242423543
# Sum of digits of 242423543 is: 29
#--------------------------------
# Enter a number: 342
# Sum of digits of 342 is: 9
#--------------------------------
# Enter a number: 09793
# Sum of digits of 9793 is: 28