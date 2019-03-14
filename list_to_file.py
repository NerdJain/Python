def main():
	n = int(input("Enter no. of items: "))
	l = []
	for i in range(n):
		l.append(input("\nEnter item: "))

	with open('p3.txt', 'w') as f:
		f.writelines(["%s\n" % item  for item in l])
if __name__ == '__main__':
	main()