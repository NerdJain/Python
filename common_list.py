def main():
	
	print("...List 1...")
	n = int(input("Enter no. of items: "))
	l1 = []
	for i in range(n):
		num = input("Enter element: ")
		l1.append(num)

	print("...List 2...")
	n = int(input("Enter no. of items: "))
	l2 = []
	for i in range(n):
		num = input("Enter element: ")
		l2.append(num)


	print("\n...List 1...")
	print(l1)
	print("\n...List 2...")
	print(l2)
	
	common = []
	print("\nCommon Items")
	for item in l1:
		if item in l2:
			common.append(item)
		else:
			continue
	print(common)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python common_list.py
# ...List 1...
# Enter no. of items: 5
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# ...List 2...
# Enter no. of items: 8
# Enter element: 4
# Enter element: 7
# Enter element: 3
# Enter element: 7
# Enter element: 9
# Enter element: python
# Enter element: 56
# Enter element: 4

# ...List 1...
# ['1', '2', '3', '4', '5']

# ...List 2...
# ['4', '7', '3', '7', '9', 'python', '56', '4']

# Common Items
# ['3', '4']