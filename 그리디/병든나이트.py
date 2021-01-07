if __name__ == '__main__':
    n,m=map(int,input().split())
    res=0
    if n==1:
        res=1
    elif n==2:
        res=min(4,(m+1//2))
    elif m<7:
        res=min(4,m)

    else:
        res=m-7+5
    print(res)