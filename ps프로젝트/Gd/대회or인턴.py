if __name__ == '__main__':
    n,m,k=map(int,input().split())

    res=0

    while True:
        n-=2
        m-=1

        if n<0 or m<0 or (n+m)<k:
            break
        res+=1
    print(res)