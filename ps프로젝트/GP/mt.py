def dfs(v):
    global cnt
    visit[v]=1
    if cnt==k:
        return

    for tm


if __name__ == '__main__':
    n,k=map(int,input().split())
    graph=[[]for _ in range(n+1)]


    arr=[0]+list(map(int,input().split()))

    for i in range(1,n+1):
        graph[i].append(arr[i])

    for i in range(1,n+1):
        visit = [0] * (n + 1)
        cnt=0
        if graph[i] and not visit[i]:
            cnt+=1
            dfs(i)