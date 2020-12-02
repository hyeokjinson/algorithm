from copy import deepcopy

dx=[0,1,0,-1]
dy=[-1,0,1,0]
xdx=[[-1,1,-1,1,-1,1,-2,2,0,0],[-1,1,-1,1,-1,1,-2,2,0,0],[0,0,1,1,2,2,1,1,3,2],[0,0,-1,-1,-2,-2,-1,-1,-3,-2]]
ydy=[[0,0,1,1,2,2,1,1,3,2],[0,0,-1,-1,-2,-2,-1,-1,-3,-2],[-1,1,-1,1,-1,1,-2,2,0,0],[-1,1,-1,1,-1,1,-2,2,0,0]]
percent=[1,1,7,7,10,10,2,2,5]

def change_dir(d):
    if d==0:return 1
    if d==1:return 2
    if d==2:return 3
    if d==3:return 0

def sprintSand(x,y,d):
    global result
    xx=x+dx[d]
    yy=y+dy[d]
    if arr[xx][yy]==0:
        return

    sand=int(arr[xx][yy])
    tmp=sand

    for i in range(9):
        nx=x+xdx[d][i]
        ny=y+ydy[d][i]
        per=percent[i]
        res=(tmp*per)//100
        if nx < 0 or ny < 0 or nx >n-1 or ny >n-1:continue
        if nx<0 or ny<0 or nx>n-1 or ny>n-1:
            result+=res
        else:
            arr[nx][ny]+=res

        sand-=res

    nx=int(x+xdx[d][9])
    ny=int(x+ydy[d][9])

    if nx<0 or ny<0 or nx>n-1 or ny>n-1:
        result+=tmp
    else:
        arr[nx][ny]+=tmp
    arr[xx][yy]=0

def solution():
    x=(n)//2
    y=(n)//2
    d=0
    m_cnt=1

    while True:

        for i in range(2):
            for j in range(m_cnt):

                sprintSand(x,y,d)
                x+=dx[d]
                y+=dy[d]
            d=change_dir(d)

        m_cnt+=1

        if m_cnt==n-1:
            for j in range(m_cnt):
                sprintSand(x,y,d)
                x+=dx[d]
                y+=dy[d]
            break


if __name__ == '__main__':
    n=int(input())
    result=0
    arr=[list(map(int,input().split()))for _ in range(n)]

    solution()

    print(result)

