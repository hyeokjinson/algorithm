def dfs(L,s):
    if L==l:
        c1,c2=0,0
        tmp=''
        for x in cb:
            if arr[x] in ck1:
                c1+=1
            else:
                c2+=1
            tmp+=arr[x]

        if c1>=1 and c2>=2:
            print(tmp)

    else:
        for i in range(s,c):
            cb[L]=i
            dfs(L+1,i+1)

if __name__ == '__main__':
    l,c=map(int,input().split())

    arr=list(map(str,input().split()))
    ck1=['a','e','i','o','u']
    arr.sort()

    cb=[0]*l

    dfs(0,0)