def main():

	n = int(input("Enter no. of items: "))
	l = []
	for i in range(n):
		num = int(input("Enter element: "))
		l.append(num)

	print("\n**List**")
	print(l,end = ' ')

	result = 1
	for item in l:
		result *= item

	print(f"\n\nMultiplication: {result}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python multiply.py
# Enter no. of items: 5
# Enter element: 2
# Enter element: 4
# Enter element: 6
# Enter element: 76
# Enter element: 3

# **List**
# [2, 4, 6, 76, 3]

# Multiplication: 10944
#------------------------------
# Enter no. of items: 6
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# Enter element: 6

# **List**
# [1, 2, 3, 4, 5, 6]

# Multiplication: 720
#-------------------------------