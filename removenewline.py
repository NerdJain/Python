def main():
	
	f = open("p1.txt",'r+')
	l1 = f.readlines()
	print(l1)
	l2 = []
	for line in l1:
		l = list(line)
		l.pop()
		line = "".join(l)
		l2.append(line)
	print(l2)
	f.writelines(l2)
	f.close()

if __name__ == '__main__':
	main()