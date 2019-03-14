#CSV to LIST and TUPLE

def main():

	sample = input("Enter Values(csv): ")
	print("Input: "+sample)
	li = sample.split(",")
	l1 = []
	for item in li:
		l1.append(int(item))
	tu = tuple(l1)
	

	print("List: ")
	print(l1)
	print("Tuple: ")
	print(tu)

if __name__ == '__main__':
	main()

#Output: 
# C:\Users\DELL\py4e>python csv.py
# Enter Values(csv): 10,20,30,40,50,60,70,80,90,100
# Input: 10,20,30,40,50,60,70,80,90,100
# List:
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Tuple:
# (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# C:\Users\DELL\py4e>python csv.py
# Enter Values(csv): 1,2,3,4,5,6,7,8,9
# Input: 1,2,3,4,5,6,7,8,9
# List:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Tuple:
# (1, 2, 3, 4, 5, 6, 7, 8, 9)