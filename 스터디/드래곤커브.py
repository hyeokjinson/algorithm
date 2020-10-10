# 규칙:
# 0커브:0
# 1커브:0,1
# 2커브:0,1,2,1/
# 3커브:0,1,2,1/,2,3,2,1
# 4커브:0,1,2,1/,2,3,2,1/,2,3,0,3,2,3,2,1
#
# 규칙성 발견: 다음 드래곤 커브 =이전 드래곤 커브 (d[-1-i]+1)%4
dx=[1,0,-1,0]
dy=[0,-1,0,1]

n=int(input())
arr=[[0]*101 for _ in range(101)]
res=0

for _ in range(n):
    curve=[]
    x,y,d,g=map(int,input().split())
    curve.append(d)
    arr[x][y]=1

    for _ in range(g):
        tmp=[]
        for i in range(len(curve)):
            tmp.append((curve[-i-1]+1)%4)
        curve.extend(tmp)

    for i in curve:
        nx=x+dx[i]
        ny=y+dy[i]
        arr[nx][ny]=1
        x,y=nx,ny
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            if arr[i+1][j] and arr[i+1][j+1] and arr[i][j+1]:
                res+=1
print(res)

