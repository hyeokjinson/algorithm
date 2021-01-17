import sys

input=sys.stdin.readline

def dfs(v):
    visit[v]=True

    for i in graph[v]:
        if not visit[i]:
            dfs(i)


if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        graph=[[] for _ in range(n+1)]
        visit=[False]*(n+1)
        for i in range(n):
            graph[i+1].append(arr[i])
        cnt=0
        for i in range(1,n+1):
            if not visit[i]:
                cnt += 1
                dfs(i)
        print(cnt)
