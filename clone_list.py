def main():
	
	n = int(input("Enter no. of items: "))
	l1 = []
	for i in range(n):
		num = input("Enter element: ")
		l1.append(num)

	clone_list = l1[:]
	clone_list[0] = "Python"
	clone_list[-1] = "End of list"

	print("\n...Original List...")
	print(l1)
	print("\n...Cloned List...")
	print(clone_list)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python clone_list.py
# Enter no. of items: 5
# Enter element: 3
# Enter element: 4
# Enter element: 5
# Enter element: 2
# Enter element: 89

# ...Original List...
# ['3', '4', '5', '2', '89']

# ...Cloned List...
# ['Python', '4', '5', '2', 'End of list']