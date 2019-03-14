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

	for item in l2:
		l1.append(item)

	print("\n...New List...")
	print(l1)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python append_list.py
# ...List 1...
# Enter no. of items: 5
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# ...List 2...
# Enter no. of items: 8
# Enter element: 3
# Enter element: 5
# Enter element: 54
# Enter element: 33
# Enter element: 67
# Enter element: 5
# Enter element: 23
# Enter element: 0

# ...New List...
# ['1', '2', '3', '4', '5', '3', '5', '54', '33', '67', '5', '23', '0']