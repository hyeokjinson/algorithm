import heapq

if __name__ == '__main__':
    n,m=map(int,input().split())

    num=[0]*(n+1)
    graph=[[]for _ in range(n+1)]
    q=[]
    res=[]

    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        num[b]+=1

    for i in range(1,n+1):
        if num[i]==0:
            heapq.heappush(q,i)

    while q:
        tmp=heapq.heappop(q)
        res.append(tmp)

        for i in graph[tmp]:
            num[i]-=1
            if num[i]==0:
                heapq.heappush(q,i)
    for x in res:
        print(x,end=' ')