import heapq
import sys

def dijkstra(start):
    q=[]
    heapq.heappush(q,[0,start])
    res=[0 for _ in range(n+1)]
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                res[i[0]]=now
                heapq.heappush(q,[cost,i[0]])
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [2147000000 for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    res = dijkstra(1)
    print(n-1)
    for i in range(2,n+1):
        print(i,res[i])




