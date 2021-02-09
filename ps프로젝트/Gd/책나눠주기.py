if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        n,m=map(int,input().split())

        arr=[]

        for _ in range(m):
            a,b=map(int,input().split())
            arr.append((a,b))

        arr.sort(key=lambda x:x[1])

        res=[0]*(n+1)

        for s,e in arr:
            for j in range(s,e+1):
                if res[j]==0:
                    res[j]=1
                    break
        print(sum(res))