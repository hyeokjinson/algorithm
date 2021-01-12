from collections import deque

n=int(input())
arr=list(map(int,input().split()))

idx=0
c_n=n
for i in range(c_n):
    print(idx+1,end=' ')
    move=arr[idx]

    if move>0:
        move-=1
    arr.remove(arr[idx])
    idx+=move

    n-=1
    if n==0:
        break
    if idx<0:
        idx=n+idx%n
    idx%=n




