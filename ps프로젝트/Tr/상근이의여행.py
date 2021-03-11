from collections import deque
import sys

input=sys.stdin.readline
def bfs(node):
    global cnt

    q=deque()

    q.append(node)
    visit[node]=1

    while q:
        x=q.popleft()

        for tmp in tree[x]:
            if visit[tmp]==0:
                visit[tmp]=1
                cnt+=1
                q.append(tmp)

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n,m=map(int,input().split())
        tree=[[] for _ in range(n+1)]
        visit=[0 for _ in range(n+1)]

        for i in range(m):
            a,b=map(int,input().split())
            tree[a].append(b)
            tree[b].append(a)
        cnt=0
        bfs(1)
        print(cnt)