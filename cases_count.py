def cases_count(s):
	print(f"\nString: {s}\n")
	lc = 0
	uc = 0
	for ch in s:
		if ch.islower():
			lc += 1
		else:
			uc += 1
	return uc,lc

def main():
	s = input("Enter a string: ")
	uc , lc = cases_count(s)
	print(f"Upper Case Letters: {uc}\nLower Case Letters: {lc}")

if __name__ == '__main__':
	main()

# Output: 
# C:\Users\DELL\py4e>python cases_count.py
# Enter a string: AbhiSHEk

# String: AbhiSHEk

# Upper Case Letters: 4
# Lower Case Letters: 4
