from _collections import deque
import sys
input=sys.stdin.readline

def bfs(start):
    q=deque([start])
    visit=[0]*(n+1)
    visit[start]=1
    cnt=0

    while q:
        tmp=q.popleft()
        cnt+=1

        for x in graph[tmp]:
            if not visit[x]:
                q.append(x)
                visit[x]=1
    return cnt



if __name__ == '__main__':
    n,m=map(int,input().split())

    graph=[[] for _ in range(n+1)]

    for i in range(m):
        a,b=map(int,input().split())
        graph[b].append(a)

    res=[]

    for i in range(1,n+1):
        res.append((bfs(i),i))

    res.sort(key=lambda x:(-x[0],x[1]))

    max_cnt=res[0][0]

    for r in res:
        if r[0]==max_cnt:
            print(r[1],end=' ')
        else:
            break