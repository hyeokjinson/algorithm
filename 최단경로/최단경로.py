import heapq
import sys

input=sys.stdin.readline
def dijsktra(start):
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
    v,e=map(int,input().split())
    start=int(input())
    graph=[[]for _ in range(v+1)]
    distance=[50000000]*(v+1)
    for i in range(e):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))

    dijsktra(start)

    for i in range(1,v+1):
        if distance[i]==50000000:
            print("INF")
        else:
            print(distance[i])