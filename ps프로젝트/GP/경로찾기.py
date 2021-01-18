def dfs(v):
    for i in range(n):
        if not visit[i] and s[v][i]==1:
            visit[i]=True
            dfs(i)

if __name__ == '__main__':
    n=int(input())
    s=[list(map(int,input().split()))for _ in range(n)]
    visit = [False for _ in range(n)]
    for i in range(n):
        dfs(i)
        for j in range(n):
            if visit[j]:
                print(1,end=' ')
            else:
                print(0,end=' ')
        print()
        visit = [False for _ in range(n)]