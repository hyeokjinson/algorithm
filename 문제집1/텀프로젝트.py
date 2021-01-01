import sys
sys.setrecursionlimit(10**7)
def dfs(x):
    global res
    visit[x]=True
    cycle.append(x)
    number=num[x]

    if visit[number]:
        if number in cycle:
            res+=cycle[cycle.index(number):]
        return
    else:
        dfs(number)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        num=[0]+list(map(int,input().split()))
        visit=[True]+[False]*n
        res=[]

        for i in range(1,n+1):
            if not visit[i]:
                cycle=[]
                dfs(i)
        print(n-len(res))