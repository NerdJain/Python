def main(arr):
    l1 = list(set(list(arr)))
    for item in l1:
    	if item == max(l1):
    		l1.remove(max(l1))
    print(max(l1))
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    main(arr)