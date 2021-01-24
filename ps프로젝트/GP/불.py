from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def bfs(x,y):
    person_xy.append((x,y))
    check[x][y]=1

    while person_xy:
        qlen=len(person_xy)

        while qlen:
            c_x,c_y=person_xy.popleft()

            for i in range(4):
                nx=c_x+dx[i]
                ny=c_y+dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if arr[nx][ny]=='.' and check[nx][ny]==0:
                        check[nx][ny]=check[c_x][c_y]+1
                        person_xy.append((nx,ny))
                elif (nx<0 or ny<0 or nx>=h or ny>=w):
                    print(check[c_x][c_y])
                    return
            qlen-=1
        fire()
    print("IMPOSSIBLE")


def fire():
    qlen=len(fire_xy)

    while qlen:
        x,y=fire_xy.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<h and 0<=ny<w:
                if arr[nx][ny]=='.':
                    arr[nx][ny]='*'
                    fire_xy.append((nx,ny))
        qlen-=1


if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        w,h=map(int,input().split())
        arr=[list(map(str,input().rstrip()))for _ in range(h)]
        check=[[0]*w for _ in range(h)]
        fire_xy=deque()
        person_xy=deque()

        for i in range(h):
            for j in range(w):
                if arr[i][j]=='@':
                    x,y=i,j
                    arr[i][j]='.'
                if arr[i][j]=='*':
                    fire_xy.append((i,j))
        fire()
        bfs(x,y)


