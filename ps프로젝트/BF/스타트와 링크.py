import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline

def dfs(L,cnt):
    global ans
    if cnt==k:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if ch[i] and ch[j]:
                    start+=arr[i][j]
                elif not ch[i] and not ch[j]:
                    link+=arr[i][j]
        ans=min(ans,abs(start-link))

    for i in range(L,n):
        if ch[i]:
            continue
        ch[i]=1
        dfs(i+1,cnt+1)
        ch[i]=0


if __name__ == '__main__':
    n=int(input())

    arr=[list(map(int,input().split()))for _ in range(n)]

    
    ch=[0for _ in range(n)]
    k=n//2
    ans=2147000000
    dfs(0,0)
    print(ans)