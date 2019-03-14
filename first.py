# x = 5
# if x > 4:
# 	print("hello")
	

# 	print("world")
	
# x = 5
# if x <= 1:
# 	print("hey")

# if 41 > 41:
# 	print("Yes")
# else:
# 	print("No")


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = float(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Maximum is", int(largest))
print("Minimum is", int(smallest))