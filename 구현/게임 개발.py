dx=[0,1,0,-1]
dy=[-1,0,1,0]
def turn_left():
    global d
    d-=1
    if d==-1:
        d=3

n,m=map(int,input().split())
x,y,d=map(int,input().split())

arr=[list(map(int,input().split()))for _ in range(n)]
ch=[[0]*m for _ in range(n)]
cnt=1
turn_time=0
ch[x][y]=1
while True:
    turn_left()
    nx=x+dx[d]
    ny=y+dy[d]

    if arr[nx][ny]==0 and ch[nx][ny]==0:
        ch[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn_time=0
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if arr[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0
print(cnt)
