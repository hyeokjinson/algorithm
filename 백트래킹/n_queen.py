def solve(x):
    global res

    if x==n:
        res+=1
        return
    for i in range(n):
        if not (a[i] or b[x+i] or c[x-i+n-1]):
            a[i]=b[x+i]=c[x-i+n-1]=True
            solve(x+1)
            a[i] = b[x+i] = c[x-i+n - 1] = False

if __name__ == '__main__':
    n=int(input())
    res=0
    a,b,c=[False]*n,[False]*(2*n-1),[False]*(2*n-1)

    solve(0)
    print(res)