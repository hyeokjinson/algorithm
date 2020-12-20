import heapq

def dijkstra(start):
    q=[]
    heapq.heappush(q,(1,start))
    dis[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if dis[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]

            if cost<dis[i[0]]:
                dis[i[0]]=cost
                print(i[0])
                heapq.heappush(q,(cost,i[0]))


if __name__ == '__main__':
    n,p,k=map(int,input().split())
    graph=[[]for i in range(n+1)]
    dis=[2147000000]*(n+1)

    for _ in range(p):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    dijkstra(1)

    print(dis)