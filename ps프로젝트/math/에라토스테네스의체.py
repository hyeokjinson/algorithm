if __name__ == '__main__':
    n,k=map(int,input().split())

    check=[False]*(n+1)
    cnt=0
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            if check[j]==False:
                check[j]=True
                cnt+=1
                if cnt==k:
                    print(j)
                    break