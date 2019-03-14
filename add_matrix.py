def add(m1,m2,r,c):

	m3 = [[(int(m1[i][j]) + int(m2[i][j])) for j in range(r)] for i in range(c)]
	return m3
	
def create_matrix(r,c):

	l = []
	for i in range(r):
		l1 = []
		for j in range(c):
			e = input("Enter element: ")
			l1.append(e)
		l.append(l1)
	return l

def main():
	r = int(input("Enter no. of rows: "))
	c = int(input("Enter no. of columns: "))

	print("Enter 1st matrix: ")
	m1 = create_matrix(r,c)
	print("Enter 2nd matrix: ")
	m2 = create_matrix(r,c)
	res = add(m1,m2,r,c)
	print("\n**Result**\n")
	for r in res:
		print(r)

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python add_matrix.py
# Enter no. of rows: 2
# Enter no. of columns: 2
# Enter 1st matrix:
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter 2nd matrix:
# Enter element: 4
# Enter element: 3
# Enter element: 2
# Enter element: 1

# **Result**

# [5, 5]
# [5, 5]