from collections import deque
import sys

input=sys.stdin.readline

def bfs(n):
    c[n]=1
    q.append(n)

    while q:
        tmp=q.popleft()

        for child in graph[tmp]:
            if c[child]==0:
                c[child]=-1*c[tmp]
                q.append(child)
            elif c[child]==c[tmp]:
                return 1
    return 0
if __name__ == '__main__':
    k=int(input())

    for _ in range(k):
        v,e=map(int,input().split())
        graph=[[]for _ in range(v+1)]
        c=[0 for _ in range(v+1)]
        q = deque()

        for _ in range(e):
            a,b=map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
        res=0
        for i in range(1,v+1):
            if c[i]==0:
                res=bfs(i)
                if res==1:
                    break
        if res==0:
            print("YES")
        else:
            print('NO')