from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y):
    animal_xy.append((x,y))
    check[x][y]=1
    while animal_xy:
        qlen=len(animal_xy)

        while qlen:
            c_x,c_y=animal_xy.popleft()

            for i in range(4):
                nx=c_x+dx[i]
                ny=c_y+dy[i]

                if 0<=nx<r and 0<=ny<c:
                    if arr[nx][ny]=='.' and check[nx][ny]==0:
                        check[nx][ny]=check[c_x][c_y]+1
                        animal_xy.append((nx,ny))
                    elif arr[nx][ny]=='D':
                        print(check[c_x][c_y])
                        return
            qlen-=1
        water()
    print("KAKTUS")

def water():
    qlen=len(water_xy)

    while qlen:
        x,y=water_xy.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<r and 0<=ny<c:
                if arr[nx][ny]=='.':
                    arr[nx][ny]='*'
                    water_xy.append((nx,ny))
        qlen-=1





if __name__ == '__main__':
    r,c=map(int,input().split())
    arr=[list(map(str,input().strip()))for _ in range(r)]
    check=[[0]*c for _ in range(r)]

    water_xy=deque()
    animal_xy=deque()

    for i in range(r):
        for j in range(c):
            if arr[i][j]=='S':
                x,y=i,j
                arr[i][j]='.'
            if arr[i][j]=='*':
                water_xy.append((i,j))

    water()
    bfs(x,y)
