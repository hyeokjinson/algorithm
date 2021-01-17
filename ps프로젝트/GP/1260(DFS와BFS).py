from collections import deque

def dfs(v):
    print(v,end=' ')
    visit[v] = True
    for x in graph[v]:
        if not visit[x]:
            dfs(x)
def bfs(v):
    q=deque([v])

    while q:
        tmp=q.popleft()
        if not visit[tmp]:
            visit[tmp]=True
            print(tmp,end=' ')
            for e in graph[tmp]:
                if not visit[e]:
                    q.append(e)




if __name__ == '__main__':
    n,m,v=map(int,input().split())
    graph=[[]for _ in range(n+1)]
    visit=[False]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for x in graph:
        x.sort()
    dfs(v)
    print()
    visit = [False] * (n + 1)
    bfs(v)
