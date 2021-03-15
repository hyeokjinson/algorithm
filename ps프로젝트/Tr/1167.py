import heapq

def dijkstra(start):
    q=[]
    dis=[2147000000 for _ in range(v+1)]
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
    v=int(input())
    graph=[[] for _ in range(v+1)]

    for _ in range(v):
        arr=list(map(int,input().split()))
        x=arr[0]

        for i in range(1,len(arr),2):
            if arr[i]==-1:
                break
            graph[x].append([arr[i],arr[i+1]])

    res=dijkstra(1)
    max_=-2147000000

    print(max(dijkstra(res.index(max(res[1:])))[1:]))