
def main():
	
	n = int(input("Enter no. of key-value pairs: "))
	dic = {}
	for i in range(n):
		key = input("Enter key: ")
		value = input("Enter value: ")
		dic[key] = value
	print(f"Dictionary: {dic}")

	print("Unique values...")
	l = list(set(dic.values()))
	print(l)

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python unique_values_dict.py
# Enter no. of key-value pairs: 5
# Enter key: 1
# Enter value: 2
# Enter key: a
# Enter value: b
# Enter key: 3
# Enter value: 2
# Enter key: 5
# Enter value: 6
# Enter key: c
# Enter value: b
# Dictionary: {'1': '2', 'a': 'b', '3': '2', '5': '6', 'c': 'b'}
# Unique values...
# ['6', 'b', '2']