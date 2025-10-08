from collections import deque

def bfs(yy,xx):
    q=deque()
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    q.append((yy,xx,0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[yy][xx]=1

    while q:
        sy,sx,num=q.popleft()
        check_flag = 0
        for i in range(4):
            nx=sx+dx[i]
            ny=sy+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx]==0 and matrix[ny][nx]!=0:
                visited[ny][nx]=1
                check_flag=1
                q.append((ny,nx,num+1))
        #print(sy, sx, num)
        if check_flag==0:
            answer.append((num,matrix[sy][sx]+matrix[y][x]))





if __name__ == '__main__':
    n,m=map(int,input().split())
    matrix=[list(map(int,input().split()))for _ in range(n)]
    answer=[]

    for y in range(n):
        for x in range(m):
            if matrix[y][x]:
                #print(y, x)
                bfs(y,x)
    answer.sort(key=lambda x:(x[0],x[1]),reverse=True)

    print(answer[0][1])
