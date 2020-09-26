from _collections import deque

if __name__=="__main__":
    n,m,k,x=map(int,input().split())
    arr=[[] for _ in range(n+1)]

    for _ in range(m):
        a,b=map(int,input().split())
        arr[a].append(b)

    print(arr)
    dis=[-1]*(n+1)
    dis[x]=0
    q=deque([x])
    while q:
        tmp=q.popleft()
        for next_node in arr[tmp]:
            if dis[next_node]==-1:
                dis[next_node]=dis[tmp]+1
                q.append(next_node)
    check=False
    for i in range(1,n+1):
        if dis[i]==k:
            print(i)
            check=True
    if not check:
        print(-1)