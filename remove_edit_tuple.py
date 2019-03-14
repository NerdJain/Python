def main():

	t1 = ()
	n = int(input("Enter no. of elements in tuple: "))
	for i in range(n):
		t1 = t1 + (input("Enter Element: "),)

	print(f"Tuple: {t1}\n")

	l = list(t1)
	print("Editing the 1st element...")
	l[0] = "Abhishek"
	t1 = tuple(l)
	print(f"Tuple: {t1}\n")	
	
	print("Removing element...")
	l.pop(-3)
	t1 = tuple(l)
	print(f"Tuple: {t1}\n")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python remove_edit_tuple.py
# Enter no. of elements in tuple: 6
# Enter Element: 1
# Enter Element: 2
# Enter Element: 3
# Enter Element: 4
# Enter Element: 5
# Enter Element: 6
# Tuple: ('1', '2', '3', '4', '5', '6')

# Editing the 1st element...
# Tuple: ('Abhishek', '2', '3', '4', '5', '6')

# Removing element...
# Tuple: ('Abhishek', '2', '3', '5', '6')