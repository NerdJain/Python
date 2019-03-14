from itertools import permutations

def main():
	
	n = int(input("Enter no. of items: "))
	l1 = []
	for i in range(n):
		num = int(input("Enter element: "))
		l1.append(num)

	for item in permutations(l1):
		print(item)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python permutations_list.py
# Enter no. of items: 4
# Enter element: 4
# Enter element: 5
# Enter element: 7
# Enter element: 9
# (4, 5, 7, 9)
# (4, 5, 9, 7)
# (4, 7, 5, 9)
# (4, 7, 9, 5)
# (4, 9, 5, 7)
# (4, 9, 7, 5)
# (5, 4, 7, 9)
# (5, 4, 9, 7)
# (5, 7, 4, 9)
# (5, 7, 9, 4)
# (5, 9, 4, 7)
# (5, 9, 7, 4)
# (7, 4, 5, 9)
# (7, 4, 9, 5)
# (7, 5, 4, 9)
# (7, 5, 9, 4)
# (7, 9, 4, 5)
# (7, 9, 5, 4)
# (9, 4, 5, 7)
# (9, 4, 7, 5)
# (9, 5, 4, 7)
# (9, 5, 7, 4)
# (9, 7, 4, 5)
# (9, 7, 5, 4)