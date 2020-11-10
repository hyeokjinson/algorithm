from _collections import deque

if __name__ == '__main__':
    n=int(input())
    tree=[[]for _ in range(n+1)]
    visited=[0]*(n+1)

    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    q=deque([1])
    visited[1]=True
    while q:
        tmp=q.popleft()

        for child in tree[tmp]:
            if not visited[child]:
                q.append(child)
                visited[child] = tmp

    for i in range(2,n+1):
        print(visited[i])