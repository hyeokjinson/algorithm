from _collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def move(x,y):
    cnt=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and arr[nx][ny]!=-1:
            dis[nx][ny]+=(arr[x][y]//5)
            cnt+=1
    arr[x][y]=arr[x][y]-(arr[x][y]//5)*cnt


r,c,t=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(r)]
time=0
while time<t:
    dis = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0:
                move(i,j)           #이동
    for i in range(r):
        for j in range(c):
            arr[i][j]+=dis[i][j]    #합치기

    ro1=0
    for i in range(r):
        if arr[i][0]==-1:
            ro1=i                 #공기청정기 찾기
            break
    rotate_array=[[-2]*c for _ in range(r)]
    for y in range(1,c):
        rotate_array[0][y-1]=arr[0][y]
        rotate_array[ro1][y]=arr[ro1][y-1]
        rotate_array[ro1][1]=0
    for i in range(1,ro1+1):
        if arr[i][0]!=-1:
            rotate_array[i][0]=arr[i-1][0]
        rotate_array[i-1][c-1]=arr[i][c-1]

    for y in range(1,c):
        rotate_array[r-1][y-1]=arr[r-1][y]
        rotate_array[ro1+1][y]=arr[ro1+1][y-1]
        rotate_array[ro1+1][1]=0
    for i in range(ro1+2,r):
        if arr[i-1][0]!=-1:
            rotate_array[i-1][0]=arr[i][0]
        rotate_array[i][c-1]=arr[i-1][c-1]
    for i in range(r):
        for j in range(c):
            if rotate_array[i][j]!= -2:
                arr[i][j]=rotate_array[i][j]
    time+=1
sum_=0
for i in range(r):
    for j in range(c):
        sum_+=arr[i][j]
print(sum_+2)
