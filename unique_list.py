def unique(l):
	
	return list(set(l))

def main():
	l = []
	n = int(input("Enter no. of elements: "))
	for i in range(n):
		l.append(input("Enter element: "))

	print(f"Original List: {l}")
	l1 = unique(l)
	print(f"New List: {l1}")

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python unique_list.py
# Enter no. of elements: 5
# Enter element: 1
# Enter element: 1
# Enter element: 3
# Enter element: 4
# Enter element: 3
# Original List: ['1', '1', '3', '4', '3']
# New List: ['4', '3', '1']