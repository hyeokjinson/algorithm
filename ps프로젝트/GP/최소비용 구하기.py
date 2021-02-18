import heapq
import sys

input=sys.stdin.readline
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

if __name__ == '__main__':
    n=int(input())
    m=int(input())

    graph=[[] for _ in range(n+1)]
    distance=[2147000000]*(n+1)

    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
    start,end=map(int,input().split())
    dijkstra(start)

    print(distance[end])