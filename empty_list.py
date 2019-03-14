def main():
	
	l = []
	#1st List
	l1 = [1,2,'3',4.7,5]
	l.append(l1)

	#2nd list
	l2 = []
	l.append(l2)
	
	#3rd list
	l3 = ['A','b','h','i','s','h','e','k']
	l.append(l3)
	
	#4th list
	l4 = ["Python","Numpy","Pandas","Lambda"]
	l.append(l4)
	
	#5th list
	l5 = []
	l.append(l5)
	
	for item in l:
		print("\nList")
		print(item,end = ' ')
		if len(item):
			print("\nNot Empty")
		else:
			print("\nEmpty")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python empty_list.py

# List
# [1, 2, '3', 4.7, 5]
# Not Empty

# List
# []
# Empty

# List
# ['A', 'b', 'h', 'i', 's', 'h', 'e', 'k']
# Not Empty

# List
# ['Python', 'Numpy', 'Pandas', 'Lambda']
# Not Empty

# List
# []
# Empty