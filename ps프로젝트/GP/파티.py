import sys
import heapq

def dijkstra(start,graph,distance):
    q=[]
    heapq.heappush(q,[0,start])
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

if __name__ == '__main__':
    n,m,x=map(int,input().split())

    graph=[[] for _ in range(n+1)]
    r_graph=[[] for _ in range(n+1)]
    distance1=[2147000000]*(n+1)
    distance2=[2147000000]*(n+1)
    for _ in range(m):
        s,e,v=map(int,input().split())
        graph[s].append((e,v))
        r_graph[e].append((s,v))

    max_=0

    dijkstra(x,graph,distance1)
    dijkstra(x,r_graph,distance2)

    for i in range(1,n+1):
        max_=max(max_,distance1[i]+distance2[i])
    print(max_)

