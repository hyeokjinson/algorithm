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
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
############################################################################################역추적
                path[i[0]]=[]
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])



if __name__ == '__main__':
    n=int(input())
    m=int(input())
    INF=2147000000

    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)

    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))

    start,end=map(int,input().split())
    path=[[]for _ in range(n+1)]
    path[start].append(start)
    res=dijkstra(start)

    print(distance[end])
    print(len(path[end]))
    print(' '.join(map(str,path[end])))