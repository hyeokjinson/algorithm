from collections import deque

if __name__ == '__main__':
    n=int(input())
    tree=[[]for _ in range(n+1)]
    parent=[0]*(n+1)
    parent[1]=1
    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

    q=deque([1])

    while q:
        tmp=q.popleft()

        for child in tree[tmp]:
            if not parent[child]:
                parent[child]=tmp
                q.append(child)
    for x in parent[2:]:
        print(x)
