import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
dy=[[0]*n for _ in range(n)]
for i in range(n):
    dy[i][i]=1
for i in range(n-1):
    if arr[i]==arr[i+1]:
        dy[i][i+1]=1
for i in range(2,n):
    for j in range(n-i):
        if arr[j]==arr[j+i] and dy[j+1][i+j-1]==1:
            dy[j][j+i]=1
m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    print(dy[x-1][y-1])