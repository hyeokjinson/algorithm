from collections import deque

def bfs(x):
    q=deque()
    q.append(x)
    visit[x]=True
    cnt=0
    while q:
        now=q.popleft()

        for tmp in graph[now]:
            if not visit[tmp]:
                cnt+=1
                visit[tmp]=True
                q.append(tmp)
    return cnt


if __name__ == '__main__':
    n=int(input())
    t=int(input())
    graph=[[] for _ in range(n+1)]
    visit=[False]*(n+1)
    for _ in range(t):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))