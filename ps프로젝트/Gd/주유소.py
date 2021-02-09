if __name__ == '__main__':
    n=int(input())

    length=list(map(int,input().split()))
    coin=list(map(int,input().split()))

    min_=2147000000
    total=0
    for i in range(n-1):
        if i==0:
           total+=length[0]*coin[0]
           min_=min(min_,coin[i])
        else:
            min_=min(min_,coin[i])
            total+=min_*length[i]
    print(total)