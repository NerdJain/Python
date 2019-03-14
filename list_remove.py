def main():
	
	n = int(input("Enter no. of items: "))
	l1 = []
	for i in range(n):
		num = input("Enter element: ")
		l1.append(num)

	print(l1)
	l1[0:1] = []
	l1[3:4] = []
	l1[3:4] = []
	print(l1)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python list_remove.py
# Enter no. of items: 8
# Enter element: 4
# Enter element: 5
# Enter element: 7
# Enter element: 3
# Enter element:
# Enter element: 6
# Enter element: 45
# Enter element: 78
# ['4', '5', '7', '3', '', '6', '45', '78']
# ['5', '7', '3', '45', '78']