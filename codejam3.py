import heapq

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dijkstra(x1,y1,x,y):
    q=[]
    distance[x][y]=0
    heapq.heappush(q,(0, x1, y1,x,y))

    while q:
        dist,c_x,c_y,x,y=heapq.heappop(q)

        if (c_x==x-1 and c_y==y):
            break
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<500 and 0<=ny<500 and distance[nx][ny]==2147000000:
                distance[nx][ny]=dist
                heapq.heappush(q,(dist+1,nx,ny))
    return dist


def dijkstra1(x1, y1, x, y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q, (0, x1, y1,x,y))

    while q:
        dist, c_x, c_y,x,y = heapq.heappop(q)

        if (c_x == x+1 and c_y == y):
            break

        for i in range(4):
            nx = c_x + dx[i]
            ny = c_y + dy[i]
            if 0 <= nx < 500 and 0 <= ny < 500 and distance[nx][ny] == 2147000000:
                distance[nx][ny] = dist
                heapq.heappush(q, (dist + 1, nx, ny))
    return dist

if __name__ == '__main__':
    T=int(input())

    for i in range(T):
        n=int(input())
        location=[]
        matrix = [[0] * 500 for _ in range(500)]
        for j in range(n):
            x,y=map(int,input().split())
            matrix[x][y]=1
            location.append((x,y))
        location.sort()
        x,y=location[len(location)//2]

        min_=2147000000

        for x,y in location:
            distance = [[2147000000] * 500 for _ in range(500)]
            for x1,y1 in location:
                if x1==x and y1==y:
                    continue
                #print(dijkstra(x1,y1,x,y),dijkstra1(x1,y1,x,y))
                min_=min(dijkstra1(x1,y1,x,y),min_)
        print(min_)