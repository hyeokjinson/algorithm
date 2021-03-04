def dfs(L,cnt):
    if cnt==6:
        for i in range(k):
            if ch[i]:
                print(a[i],end=' ')
        print()
        return

    for i in range(L,k):
        ch[i]=1
        dfs(i+1,cnt+1)
        ch[i]=0

while True:
    a=list(map(int,input().split()))
    k=a[0]
    a=a[1:]

    if k==0:
        break

    ch=[0 for _ in range(k)]
    dfs(0,0)
    print()