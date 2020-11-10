import heapq
import sys

input=sys.stdin.readline
def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)

        if now==k:
            break
        if 0<=now*2<100001 and distance[now*2]==2147000000:
            distance[now*2]=distance[now]
            heapq.heappush(q,(distance[now*2],now*2))
        for i in (now-1,now+1):
            if 0<=i<100001 and distance[i]==2147000000:
                distance[i]=distance[now]+1
                heapq.heappush(q,(distance[i],i))



if __name__ == '__main__':
    n,k=map(int,input().split())
    distance=[2147000000]*(100001)
    dijkstra(n)

    # for i in range(k+1):
    #     print(distance[i],end=' ')
    print(distance[k])