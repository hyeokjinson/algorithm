import heapq

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist-i[1]+arr[i[0]]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


if __name__ == '__main__':
    n,start,end,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]

    distance=[1000000]*(n+1)

    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
    arr=list(map(int,input().split()))

    dijkstra(start)

    print(distance[end])