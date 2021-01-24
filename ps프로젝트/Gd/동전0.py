if __name__ == '__main__':
    n,k=map(int,input().split())

    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    cnt=0
    for i in range(1,n+1):
        coin=arr[-i]

        if k>=coin:
            num=k//coin
            k-=num*coin
            cnt+=num
    print(cnt)