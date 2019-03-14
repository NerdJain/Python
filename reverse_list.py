def reverse(l):
	
	l = l[::-1]
	return l

def main():
	l = []
	n = int(input("Enter no. of elements: "))
	for i in range(n):
		l.append(input("Enter element: "))

	print(f"Original List: {l}")
	l1 = reverse(l)
	print(f"Reversed List: {l1}")

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python reverse_list.py
# Enter no. of elements: 5
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# Original List: ['1', '2', '3', '4', '5']
# Reversed List: ['5', '4', '3', '2', '1']