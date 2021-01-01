import sys
from _collections import deque
input=sys.stdin.readline

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

# def dfs(x,y):
#     global cnt
#     cnt+=1
#     board[x][y]=0
#
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
#             dfs(nx,ny)

if __name__ == '__main__':
    # n,m=map(int,input().split())
    # board=[list(map(int,input().split())) for _ in range(n)]
    # res=[]
    #
    # for i in range(n):
    #     for j in range(m):
    #         if board[i][j]==1:
    #             cnt=0
    #             dfs(i,j)
    #             res.append(cnt)
    # print(len(res))
    # print(max(res))

    n,m=map(int,input().split())
    board=[list(map(int,input().split()))for _ in range(n)]
    res=[]
    cnt=0
    q=deque()

    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                board[i][j]=0
                q.append((i,j))
                cnt=1
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                            board[nx][ny]=0
                            q.append((nx,ny))
                            cnt+=1
                res.append(cnt)
    print(len(res))
    if len(res)==0:
        print(0)
    else:
        print(max(res))
