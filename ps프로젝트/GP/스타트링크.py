from collections import deque

def bfs():
    q.append(s-1)
    res[s-1]=1

    while q:
        x=q.popleft()

        if x==g-1:
            print(res[x]-1)
            return

        if x+u<f and not res[x+u]:
            res[x+u]=res[x]+1
            q.append(x+u)
        if x-d>=0 and not res[x-d]:
            res[x-d]=res[x]+1
            q.append(x-d)

    print("use the stairs")





if __name__ == '__main__':
    f,s,g,u,d=map(int,input().split())

    res=[0 for _ in range(f)]
    q=deque()
    bfs()