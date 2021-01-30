import heapq

def dijkstra(start):
    q=[]
    dis = [2147000000 for _ in range(v + 1)]
    heapq.heappush(q,[0,start])
    dis[start]=0

    while q:
        dist,now=heapq.heappop(q)

        for i in graph[now]:                #[1:(3,2)],[2:4],[3:1,4],[4:2,3,5],[5:4]
            cost=dist+i[1]
            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,[cost,i[0]])

    return dis


if __name__ == '__main__':
    v=int(input())

    graph=[[]for _ in range(v+1)]

    for _ in range(v):
        arr=list(map(int,input().split()))
        x=arr[0]
        for i in range(1,len(arr),2):
            if arr[i]==-1:
                break
            graph[x].append([arr[i],arr[i+1]])

    res=dijkstra(1)
    max_=-2147000000
    print(res)
    print(dijkstra(res.index(max(res[1:]))))
    print(max(dijkstra(res.index(max(res[1:])))[1:]))
    # for i in range(1,v+1):
    #     if res[i]>=max_:
    #         max_=res[i]
    #
    # print(max_)