def dfs(start):
    ch[start]=False

    dy[start][0]=1
    dy[start][1]=0

    for i in graph[start]:
        if ch[i]:
            dfs(i)
            dy[start][0]+=dy[i][1]
            dy[start][1]+=max(dy[i][0],dy[i][1])

if __name__ == '__main__':
    n=int(input())
    dy=[[0,0] for _ in range(n+1)]
    ch=[True for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1)

    print(n-max(dy[1][1],dy[1][0]))