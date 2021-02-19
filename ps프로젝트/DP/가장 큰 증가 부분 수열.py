if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,0)
    dy=[0]*(n+1)

    dy[1]=a[1]
    res=a[1]

    for i in range(1,n+1):
        max_=0
        for j in range(i-1,0,-1):
            if a[i]>a[j] and max_<dy[j]:
                max_=dy[j]

        dy[i]=max_+a[i]
        if res<dy[i]:
            res=dy[i]
    print(res)