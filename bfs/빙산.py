from _collections import deque
from copy import deepcopy
import sys
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def remove(x,y,board):
    cnt=0
    maps=deepcopy(board)
    visit = [[0] * m for _ in range(n)]
    visit[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and maps[nx][ny]==0 and visit[nx][ny]==0:
            cnt+=1
            visit[nx][ny]=1

    if board[x][y]-cnt>=0:
        board[x][y]-=cnt
    else:
        board[x][y]=0

def check():
    q=deque()
    res=[]
    maps=deepcopy(board)
    for i in range(n):
        for j in range(m):
            if maps[i][j]:
                q.append((i,j))
                cnt = 1
                while q:
                    x,y=q.popleft()

                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny]:
                            cnt+=1
                            q.append((nx,ny))
                            maps[nx][ny]=0
                res.append(cnt)

    if len(res)>1:
        return True
    return False

def check1():
    for i in range(n):
        for j in range(m):
            if board[i][j]!=0:
                return False
    return True




if __name__ == '__main__':
    n,m=map(int,input().split())
    board=[list(map(int,input().split()))for _ in range(n)]
    year=0
    while True:
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    remove(i,j,board)


        year+=1
        for i in range(n):
            for j in range(m):
                print(board[i][j], end=' ')
            print()
        if check():
            print(year)
            break
        elif check1():
            print(0)
            break



