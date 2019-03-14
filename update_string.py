def update(s,r1,r2):
	print(f"\nString: {s}\n")
	if r1 not in s:
		return "*Invalid Input*"
	else:
		l1 = list(s)
		for i in range(len(l1)):
			if l1[i] == r1:
				l1[i] = r2
	return "".join(l1)

def main():
	s = input("Enter a string: ")
	r1 = input("Enter char to replace: ")
	r2 = input("Enter char to replace with: ")
	s = update(s,r1,r2)
	print(f"Updated String: {s}")

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python update_string.py
# Enter a string: series
# Enter char to replace: e
# Enter char to replace with: c

# String: series

# Updated String: scrics