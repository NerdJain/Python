def main():
	
	n = int(input("Enter no. of items: "))
	l = []
	for i in range(n):
		num = input("Enter element: ")
		l.append(num)

	print("\n**Old List**")
	print(l)
	l = list(set(l))
	print("\n**New List**")
	print(l)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python duplicates_list.py
# Enter no. of items: 10
# Enter element: 2
# Enter element: 2
# Enter element: 5
# Enter element: 7
# Enter element: 8
# Enter element: 7
# Enter element: 5
# Enter element: 23
# Enter element: 1
# Enter element: 1

# **Old List**
# ['2', '2', '5', '7', '8', '7', '5', '23', '1', '1']

# **New List**
# ['1', '7', '23', '5', '8', '2']
	