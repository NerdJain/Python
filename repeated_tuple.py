
def main():

	l = []
	n = int(input("Enter no. of elements in tuple: "))
	for i in range(n):
		l.append(int(input("Enter Element: ")))

	t1 = tuple(l)
	t2 = ()
	for item in t1:
		if t1.count(item) > 1:
			t2 = t2 + (item,)

	print(f"Tuple: {t1}")
	print(f"Repeated elements in tuple: {set(t2)}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python repeated_tuple.py
# Enter no. of elements in tuple: 8
# Enter Element: 1
# Enter Element: 2
# Enter Element: 1
# Enter Element: 3
# Enter Element: 3
# Enter Element: 5
# Enter Element: 1
# Enter Element: 7
# Tuple: (1, 2, 1, 3, 3, 5, 1, 7)
# Repeated elements in tuple: {1, 3}