def main():
	
	f1 = open("p1.txt",'r')
	f2 = open("p2.txt",'w')

	ch = f1.read()
	f2.write(ch)

	f1.close()
	f2.close()

	
if __name__ == '__main__':
	main()