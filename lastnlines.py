def main():
	
	f = open("p1.txt",'r')
	n = int(input("Enter no. of last lines: "))
	c = 0
	l = []
	for line in f.readlines():
		c += 1
		l.append(line)
	print(f"Last {n} lines: \n")
	for i in range(c-n,c):
		print(l[i])
	f.close()
	
if __name__ == '__main__':
	main()