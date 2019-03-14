def main():
	
	n = int(input("Enter no. of items: "))
	l1 = []
	for i in range(n):
		num = int(input("Enter element: "))
		l1.append(num)

	print("\n...Old List...")
	print(l1)
	for item in l1:
		if not item % 2:
			l1.remove(item)

	print("\n...Odd List...")
	print(l1)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python list_remove_even.py
# Enter no. of items: 10
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# Enter element: 6
# Enter element: 7
# Enter element: 8
# Enter element: 9
# Enter element: 10

# ...Old List...
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ...Odd List...
# [1, 3, 5, 7, 9]