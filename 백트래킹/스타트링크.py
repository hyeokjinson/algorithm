from collections import deque

def bfs():
    q.append(s-1)
    c[s-1]=1
    while q:
        x=q.popleft()
        if x==g-1:
            print(c[x]-1)
            return
        if x+u<f and not c[x+u]:
            q.append(x+u)
            c[x+u]=c[x]+1
        if x-d >=0 and not c[x-d]:
            q.append(x-d)
            c[x-d]=c[x]+1
    print("use the stairs")

if __name__ == '__main__':
    f,s,g,u,d=map(int,input().split())
    c=[0 for _ in range(f)]
    q=deque()
    bfs()