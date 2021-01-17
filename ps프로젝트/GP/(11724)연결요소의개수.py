import sys
sys.setrecursionlimit(10000000)

def dfs(v):
    visit[v]=True

    for x in graph[v]:
        if not visit[x]:
            dfs(x)


if __name__ == '__main__':
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]

    visit=[False]*(n+1)

    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt=0
    for i in range(1,n+1):
        if not visit[i]:
            cnt+=1
            dfs(i)
    print(cnt)