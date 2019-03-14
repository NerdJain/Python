#Dictionary in Python

def main():
	alphabet = dict()

	ch = 1
	while ch:
		key = input("Enter Key: ")
		value = input("Enter Value: ")
		if key == value[0]:	
			alphabet[key] = value
		else:
			print("Invalid input!")

		print("\n")
		ch = input("Continue? yes/no: ")
		if ch.lower() == "yes":
			continue
		else:
			break

	print(alphabet)

if __name__ == "__main__":
	main()

#Output:
# C:\Users\DELL\py4e>python dictionary.py
# Enter Key: A
# Enter Value: Java
# Invalid input!


# Continue? yes/no: yes
# Enter Key: J
# Enter Value: Java


# Continue? yes/no: yes
# Enter Key: T
# Enter Value: Tuple


# Continue? yes/no: yes
# Enter Key: S
# Enter Value: Algorithms
# Invalid input!


# Continue? yes/no: yes
# Enter Key: S
# Enter Value: Selenium


# Continue? yes/no: no
# {'J': 'Java', 'T': 'Tuple', 'S': 'Selenium'}