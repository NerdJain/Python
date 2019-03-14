def main():

	l = []
	n = int(input("Enter no. of elements in tuple: "))
	for i in range(n):
		l.append(input("Enter Element: "))

	t1 = tuple(l)

	se = input("Enter search element: ")
	
	if se in t1:
		print(f"{se} is in {t1}")
	else:
		print(f"{se} not in {t1}")

if __name__ == '__main__':
	main()

#Output:
# Enter no. of elements in tuple: 6
# Enter Element: 2
# Enter Element: 3
# Enter Element: 45
# Enter Element: 12
# Enter Element: 78
# Enter Element: 22
# Enter search element: 44
# 44 not in ('2', '3', '45', '12', '78', '22')