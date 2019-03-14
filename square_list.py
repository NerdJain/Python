def main():
	
	l1 = []
	for i in range(1,30):
		l1.append(i**2)

	print("...List...")
	print(l1)
	l1[5:len(l1)-5] = []
	print("\n...New List...")
	print(l1)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python square_list.py
# ...List...
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841]

# ...New List...
# [1, 4, 9, 16, 25, 625, 676, 729, 784, 841]