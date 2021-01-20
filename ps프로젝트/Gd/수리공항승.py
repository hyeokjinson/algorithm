if __name__ == '__main__':
    n,l=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    tmp=0
    cnt=0
    for x in arr:
        if tmp<x:
            cnt+=1
            tmp=x+l-1
    print(cnt)