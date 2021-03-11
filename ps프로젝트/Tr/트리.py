def dfs(node):
    global cnt
    flag=False
    visit[node]=1

    for i in range(n):
        if ch[node][i]==1 and visit[i]==0:
            flag=True
            dfs(i)
    if not flag:
        cnt+=1

if __name__ == '__main__':
    n=int(input())
    tree=list(map(int,input().split()))
    node=int(input())

    ch=[[0]*n for _ in range(n)]
    visit=[0for _ in range(n)]

    for i in range(n):
        if tree[i]!=-1:
            ch[i][tree[i]]=1
            ch[tree[i]][i]=1
        else:
            root=i

    for i in range(n):
        ch[i][node]=0
        ch[node][i]=0
    cnt=0
    dfs(root)
    if node==root:
        print(0)
    else:
        print(cnt)
