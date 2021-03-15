import heapq

def dijkstra(start):
    q=[]
    dis=[2147000000 for _ in range(n+1)]
    dis[start]=0
    heapq.heappush(q,[0,start])

    while q:
        dist,now=heapq.heappop(q)

        for i in graph[now]:
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,[cost,i[0]])
    return dis
if __name__ == '__main__':
    n=int(input())
    graph=[[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b,c=map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])

    res=dijkstra(1)

    print(max(dijkstra(res.index(max(res[1:])))[1:]))