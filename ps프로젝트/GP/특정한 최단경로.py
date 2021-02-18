import heapq

def dijkstra(start):
    q=[]
    distance=[2147000000]*(n+1)

    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance

if __name__ == '__main__':
    n,e=map(int,input().split())
    graph=[[] for _ in range(n+1)]

    for _ in range(e):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    v1,v2=map(int,input().split())

    one=dijkstra(1)
    v1_array=dijkstra(v1)
    v2_array=dijkstra(v2)
    res=0
    for i in range(1,n+1):
        res=min(one[v1]+v1_array[v2]+v2_array[n],one[v2]+v2_array[v1]+v1_array[n])

    print(res if res<2147000000 else -1)