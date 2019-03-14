def roots(a,b,c):
	a = int(a)
	b = int(b)
	c = int(c)
	D = (b**2) - (4*a*c)
	if D < 0:
		return ("Complex Roots!!",None)
	elif D >= 0:
		return (int(((-b)+(D**0.5))/2*a) , int(((-b)-(D**0.5))/2*a))


def main():

	a = int(input("Enter coefficient of x^2: "))
	b = int(input("Enter coefficient of x^1: "))
	c = int(input("Enter constant value: "))

	print(f"\nQuadratic Equation: {a}x^2 + {b}x + {c}\n")
	r1,r2 = roots(a,b,c)
	if(r2 == None):
		print(r1)
	else:
		print(f"\n{r1} and {r2} are roots.")


if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python roots.py
# Enter coefficient of x^2: 1
# Enter coefficient of x^1: 3
# Enter constant value: -4

# Quadratic Equation: 1x^2 + 3x + -4


1 and -4 are roots.