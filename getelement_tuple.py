
def main():

	t1 = ()
	n = int(input("Enter no. of elements in tuple: "))
	for i in range(n):
		t1 = t1+ (int(input("Enter Element: ")),)

	
	print(f"4th element from beginning: {t1[3]}")
	print(f"4th element from end: {t1[-4]}\n")


	print(f"First Half: ")
	for i in range(len(t1)//2):
		print(t1[i],end = " ")

	print(f"\nOther Half: ")
	for i in range(len(t1)//2,n):
		print(t1[i],end = " ")

if __name__ == '__main__':
	main()

#Output: 	
# C:\Users\DELL\py4e>python getelement_tuple.py
# Enter no. of elements in tuple: 10
# Enter Element: 1
# Enter Element: 2
# Enter Element: 3
# Enter Element: 4
# Enter Element: 5
# Enter Element: 6
# Enter Element: 7
# Enter Element: 8
# Enter Element: 9
# Enter Element: 0
# 4th element from beginning: 4
# 4th element from end: 7

# First Half:
# 1 2 3 4 5
# Other Half:
# 6 7 8 9 0