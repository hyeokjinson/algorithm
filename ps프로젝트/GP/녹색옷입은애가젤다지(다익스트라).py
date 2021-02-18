import heapq
import sys

dx=[1,0,-1,0]
dy=[0,-1,0,1]

def dijkstra(x,y):
    q=[]
    distance[x][y]=matrix[x][y]
    heapq.heappush(q,(matrix[x][y],x,y))

    while q:
        dist,c_x,c_y=heapq.heappop(q)

        if c_x==n-1 and c_y==n-1:
            break

        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]

            if 0<=nx<n and 0<=ny<n and distance[nx][ny]==2147000000:
                distance[nx][ny]=dist+matrix[nx][ny]
                heapq.heappush(q,(dist+matrix[nx][ny],nx,ny))
if __name__ == '__main__':
    i=1
    while True:
        n=int(input())

        if n==0:
            break

        distance=[[2147000000]*n for _ in range(n)]
        matrix=[list(map(int,input().split())) for _ in range(n)]

        dijkstra(0,0)

        print('Problem %d: %d'%(i,distance[n-1][n-1]))
        i+=1