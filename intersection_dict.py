def main():
	
	n = int(input("Enter no. of key-value pairs: "))
	dic = {}
	for i in range(n):
		key = input("Enter key: ")
		value = input("Enter value: ")
		dic[key] = value
	print(f"Dictionary: {dic}")

	n = int(input("Enter no. of key-value pairs: "))
	dic1 = {}
	for i in range(n):
		key = input("Enter key: ")
		value = input("Enter value: ")
		dic1[key] = value
	print(f"Dictionary: {dic1}")

	k1 = set(dic.keys())
	k2 = set(dic1.keys())

	print(f"Intersection of {dic} and {dic1}: {k1&k2}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python intersection_dict.py
# Enter no. of key-value pairs: 3
# Enter key: 1
# Enter value: 2
# Enter key: 3
# Enter value: 4
# Enter key: 5
# Enter value: 6
# Dictionary: {'1': '2', '3': '4', '5': '6'}
# Enter no. of key-value pairs: 4
# Enter key: 2
# Enter value: 3
# Enter key: 4
# Enter value: 5
# Enter key: 1
# Enter value: 2
# Enter key: 78
# Enter value: 89
# Dictionary: {'2': '3', '4': '5', '1': '2', '78': '89'}
# Intersection of {'1': '2', '3': '4', '5': '6'} and {'2': '3', '4': '5', '1': '2', '78': '89'}: {'1'}