from collections import deque

def bfs(x):
    q=deque([start])
    visit=[False]*(n+1)
    visit[start]=True
    while q:
        node=q.popleft()

        for nod,w in graph[node]:
            if not visit[nod] and w>=x:
                visit[nod]=True
                q.append(nod)
    return visit[end]

if __name__ == '__main__':
    n,m=map(int,input().split())

    graph=[[] for _ in range(n+1)]
    lt=1000000000
    rt=1
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

        lt=min(lt,c)
        rt=max(rt,c)

    start,end=map(int,input().split())
    res=0
    while lt<=rt:
        mid=(lt+rt)//2

        if bfs(mid):
            res=mid
            lt=mid+1
        else:
            rt=mid-1
    print(res)
