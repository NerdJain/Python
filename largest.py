#Largest number (Abhishek - 16CSU015)
def main():
	n1 = int(input("Enter a number: "))
	n2 = int(input("Enter a number: "))
	n3 = int(input("Enter a number: "))

	print("\n")
	#Largest number
	if(n1 >= n2 and n1 >= n3):
		print(f"Largest number: {n1}")
	elif(n2 >= n1 and n2 >= n3):
		print(f"Largest number: {n2}")
	elif(n3 >= n1 and n3 >= n2):
		print(f"Largest number: {n3}")
	
	#Using max() function
	#print(max((n1,n2,n3)))

if __name__ == "__main__":
	main()


#Output:
# C:\Users\DELL\py4e>python largest.py
# Enter a number: 45
# Enter a number: -3
# Enter a number: 68

# Largest number: 68
#-------------------------
# Enter a number: -23
# Enter a number: -5
# Enter a number: -1

# Largest number: -1
#-------------------------
# Enter a number: 5
# Enter a number: 7
# Enter a number: 5

# Largest number: 7
#-------------------------
# Enter a number: 234
# Enter a number: 12
# Enter a number: 56

# Largest number: 234