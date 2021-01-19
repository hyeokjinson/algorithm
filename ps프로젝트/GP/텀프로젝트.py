def dfs(x):
    global res

    visit[x]=True
    cycle.append(x)
    num=arr[x]

    if visit[num]:
        if num in cycle:
            res+=cycle[cycle.index(num):]
        return
    else:
        dfs(num)

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[0]+list(map(int,input().split()))
        visit=[True]+[False]*n
        res=[]

        for i in range(1,n+1):
            if not visit[i]:
                cycle=[]
                dfs(i)
        print(n-len(res))