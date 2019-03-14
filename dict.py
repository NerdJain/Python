
def main():
	
	key = []
	value = []
	n = int(input("Enter no. of key-value pairs: "))

	for i in range(n):
		word = input("Enter a word: ")
		key.append(word[0])
		value.append(word)

	dic = dict(zip(key,value))
	print(f"Dictionary: {dic}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python dict.py
# Enter no. of key-value pairs: 5
# Enter a word: Abhishek
# Enter a word: python
# Enter a word: dictionary
# Enter a word: word
# Enter a word: Dell
# Dictionary: {'A': 'Abhishek', 'p': 'python', 'd': 'dictionary', 'w': 'word', 'D': 'Dell'}