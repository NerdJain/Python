def ascii(s):
	print(f"\nString: {s}\n")
	for ch in s:
		print(f"Character: {ch}\nAscii value: {ord(ch)}\n")

def main():
	s = input("Enter a string: ")
	ascii(s)

if __name__ == '__main__':
	main()

# Output: 
# C:\Users\DELL\py4e>python ascii.py
# Enter a string: AbhI 123

# String: AbhI 123 JaiN

# Character: A
# Ascii value: 65

# Character: b
# Ascii value: 98

# Character: h
# Ascii value: 104

# Character: I
# Ascii value: 73

# Character:
# Ascii value: 32

# Character: 1
# Ascii value: 49

# Character: 2
# Ascii value: 50

# Character: 3
# Ascii value: 51