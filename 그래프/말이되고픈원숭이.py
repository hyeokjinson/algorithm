from _collections import deque

h_x=[-1,-2,-2,-1,1,2,2,1]
h_y=[-2,-1,1,2,-2,-1,1,2]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def horse_move(x,y,z):
    h_route=[]
    for i in range(8):
        hx=x+h_x[i]
        hy=y+h_y[i]
        if hx<0 or hx>=h or hy<0 or hy>=w:
            continue
        if arr[hx][hy]==0:
            if ch[hx][hy][z+1]==0:
                ch[hx][hy][z+1]=ch[x][y][z]+1
                q.append((hx,hy,z+1))

def monkey_move(x,y,z):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w :
            if arr[nx][ny]==0 and ch[nx][ny][z]==0:
                ch[nx][ny][z]=ch[x][y][z]+1
                q.append((nx,ny,z))




if __name__=="__main__":
    k=int(input())
    w,h=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(h)]
    ch=[[[0]*(k+1)for _ in range(w)] for _ in range(h)]
    q=deque()
    q.append((0,0,0))
    ch[0][0][0]=1
    while q:
        x,y,z=q.popleft()
        if x==h-1 and y==w-1:
            print(ch[x][y][z]-1)
            break
        if z<k:
            horse_move(x,y,z)
            monkey_move(x,y,z)
        elif z==k:
            monkey_move(x,y,z)
    else:
        print(-1)