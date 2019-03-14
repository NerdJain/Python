
def convert(deg):

	return (float(deg) * 0.0174532925)

def main():

	d = input("Enter value in degrees: ")

	print("Converting value to radians....")
	res = convert(d)

	print(f"{d} in degress is {res} in radians.")

if __name__ == '__main__':
	main()

# Output:
# C:\Users\DELL\py4e>python degree_radian.py
# Enter value in degrees: 90
# Converting value to radians....
# 90 in degress is 1.5707963249999999 in radians.