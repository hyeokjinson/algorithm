from _collections import deque
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
m=int(input())
b=[list(map(int,input().split()))for _ in range(m)]
des=deque()
def sum1(arr,n):
    res=0
    s=0
    e=n-1
    for i in range(n):
        for j in range(s,e+1):
            res+=arr[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    return res

for i in range(m):
    cnt=b[i][2]
    idx=b[i][0]
    for j in range(cnt,0,-1):
        if b[i][1]==0:
            a[idx-1].append(a[idx-1].pop(0))

        if b[i][1]==1:
            a[idx-1].insert(0,a[idx-1].pop(-1))
print(sum1(a,n))