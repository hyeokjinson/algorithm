dx=[0,0,-1,1]
dy=[-1,1,0,0]


location=['L','R','U','D']
n=int(input())
x,y=1,1
locations=input().split()

for plan in locations:
    for i in range(4):
        if plan==location[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if 1<=nx<n and 1<=ny<n:
        x,y=nx,ny
print(x,y)

