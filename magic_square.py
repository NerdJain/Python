def main():

	c = int(input("Enter column: "))
	r = int(input("Enter row: "))

	a = [[]*c for i in range(r)]

	for i in range(r):
		for j in range(c):
			a[i].append(int(input("Enter element: ")))

	print(a)

	s = 0
	for i in range(c):
		s += a[i][i]

	for i in range(c):
		rs = 0
		for j in range(c):
			rs += a[i][j]

		if rs != s:
			print("Not a magic square!")

	for i in range(c):
		cs = 0
		for j in range(c):
			cs += a[i][j]

		if cs != s:
			print("Not a magic square!")

	print("Magic square!")

if __name__ == '__main__':
	main()