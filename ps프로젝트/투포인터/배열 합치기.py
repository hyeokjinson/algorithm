if __name__ == '__main__':
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    res=a+b
    res.sort()
    for x in res:
        print(x,end=' ')