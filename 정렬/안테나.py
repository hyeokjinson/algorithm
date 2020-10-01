n=int(input())
arr=list(map(int,input().split()))
arr.sort()
tmp=len(arr)//2-1
print(arr[tmp])