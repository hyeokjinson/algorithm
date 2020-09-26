import sys
arr=[0,1,1]
n=int(input())
if n==1:
    print(1)
    sys.exit(0)
elif n==2:
    print(1)
    sys.exit(0)

for i in range(3,n+1):
    arr.append(arr[i-2]+arr[i-1])

print(arr[n])