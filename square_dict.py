
def main():
	
	dic = {x:x**2 for x in range(1,16)}
	print(f"Dictionary: {dic}")

if __name__ == '__main__':
	main()

#Output:
# C:\Users\DELL\py4e>python square_dict.py
# Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}