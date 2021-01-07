if __name__ == '__main__':
    n,m=map(int,input().split())

    arr=[list(map(int,input().split()))for _ in range(n)]
    k=int(input())

    for _ in range(k):
        i,j,x,y=map(int,input().split())
        res=0

        for q in range(i-1,x-1):
            for e in range(j-1,y-1):
                res+=arr[q][e]
                print(res)
