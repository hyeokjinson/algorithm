import heapq

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dijkstra(x,y):
    q=[]
    heapq.heappush(q,(0,x,y))
    distance[x][y]=0

    while q:
        dist,c_x,c_y=heapq.heappop(q)
        if c_x==n-1 and c_y==m-1:
            break
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]

            if 0<=nx<n and 0<=ny<m and distance[nx][ny]==5000:
                distance[nx][ny]=dist

                if matrix[nx][ny]==1:
                    heapq.heappush(q,(dist+1,nx,ny))
                else:
                    heapq.heappush(q,(dist,nx,ny))



if __name__ == '__main__':
    m,n=map(int,input().split())

    matrix=[list(map(int,input().strip())) for _ in range(n)]
    distance=[[5000]*m for _ in range(n)]

    dijkstra(0,0)

    print(distance[n-1][m-1])
