import sys
from _collections import deque
d=[(0,1),(1,0),(0,-1),(-1,0)]
input = sys.stdin.readline

n=int(input())
k=int(input())
mat=[[0]*(n+2) for _ in range(n+2)]
for i in range(n+2):
    mat[0][i]=1
    mat[i][0]=1
    mat[i][n+1]=1
    mat[n+1][i]=1

for _ in range(k):
    a,b=map(int,input().split())
    mat[a][b]=2

L=int(input())
L_array=[]
for _ in range(L):
    x,c=input().split()
    L_array.append([int(x),c])

res=0
x,y=1,1
now=0
mat[1][1]=3
loc=deque([[1,1]])
while True:

    x=x+d[now][0]
    y=y+d[now][1]

    if mat[x][y]==2:
        mat[x][y]=3
        loc.append([x,y])
        res+=1
    elif mat[x][y]==0:
        mat[x][y]=3
        loc.append([x,y])
        del_x,del_y=loc.popleft()
        mat[del_x][del_y]=0
        res+=1
    else:
        res+=1
        break
    if len(L_array) != 0:
        if L_array[0][0]==res:
            if L_array[0][1]=='L':
                now=(now+3)%4
            elif L_array[0][1]=='D':
                now=(now+1)%4
            del L_array[0]
print(res)

