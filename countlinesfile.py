def main():
	
	f = open("p1.txt",'r')
	c = 0
	print("File Data: ")
	for line in f.readlines():
		c += 1
		print(line)
	print("----------------------")
	print(f"No. of lines: {c}\n")
	print("----------------------")
	f.close()

if __name__ == '__main__':
	main()