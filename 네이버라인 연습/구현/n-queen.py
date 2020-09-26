def check(x):
    for i in range(x):
        if arr[i]==arr[x] or x-i==abs(arr[i]-arr[x]):
            return False
    return True

def dfs(L):
    global cnt
    if L==n:
        cnt+=1
    else:
        for i in range(n):
            arr[L]=i
            if check(L):
                dfs(L+1)

        
n=int(input())
arr=[0]*n
cnt=0
dfs(0)
print(cnt)
