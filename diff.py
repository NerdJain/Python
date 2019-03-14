def calc(n = 2):
	s1 = 0
	s2 = 0
	for i in range(1,n+1):
		s2 = s2 + (i**2)
		s1 = s1 + i
	s1 = s1**2
	return (s1,s2,s1-s2)	

def main():

	n = int(input("Enter no. of natural numbers: "))

	s1,s2,diff = calc(n)

	print(f"squared sum of n no.s ({s1}) - sum of squared n no.s ({s2}) = {diff}")
	
if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python diff.py
# Enter no. of natural numbers: 5
# squared sum of n no.s (225) - sum of squared n no.s (55) = 170