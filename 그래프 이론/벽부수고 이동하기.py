import heapq

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dijkstra(x,y):
    q=[]
    distance[x][y] = 1
    heapq.heappush(q,(1,x,y,False))

    while q:
        dist,c_x,c_y,flag=heapq.heappop(q)

        if c_x==n-1 and c_y==m-1:
            break
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==0:
                    if distance[nx][ny]==2147000000 or (matrix[nx][ny]==1 and flag==False):
                        distance[nx][ny] = dist
                        heapq.heappush(q,(dist+1,nx,ny,flag))
                elif matrix[nx][ny]==1:
                    if not flag and distance[nx][ny]==2147000000:
                        distance[nx][ny]=dist+1
                        heapq.heappush(q,(dist+2,nx,ny,True))
                else:
                    heapq.heappush(q,(dist,nx,ny,flag))



if __name__ == '__main__':
    n,m=map(int,input().split())
    matrix=[list(map(int,input().strip()))for _ in range(n)]
    distance=[[2147000000]*m for _ in range(n)]

    dijkstra(0,0)
    for i in range(n):
        for j in range(m):
            print(distance[i][j],end=' ')
        print()
    if distance[n-1][m-1]==2147000000:
        print(-1)
    else:
        print(distance[n-1][m-1])
