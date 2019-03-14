#Changing elements string and tuple (Abhishek - 16CSU015)
def main():

	str_in = "To change the elements in string or tuple data structure"
	tup_in = (34,45,78,335,57,2,5575,87,457,4535)

	print(f"Input String: {str_in}")
	#Updating String
	l1 = list(str_in)
	l1 = l1[3:32]
	l1[6] = "d "
	str_in = "".join(l1)
	print(f"New String: {str_in}")
	print("\n")
	print(f"Input Tuple: {tup_in}")
	#Updating Tuple
	l2 = list(tup_in)
	l2[4] = -678
	l2[7] = 52361381
	tup_in = tuple(l2)
	print(f"New Tuple: {tup_in}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python str_tuple.py
# Input String: To change the elements in string or tuple data structure
# New String: changed the elements in string


# Input Tuple: (34, 45, 78, 335, 57, 2, 5575, 87, 457, 4535)
# New Tuple: (34, 45, 78, 335, -678, 2, 5575, 52361381, 457, 4535)