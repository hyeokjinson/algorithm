if __name__ == '__main__':
    t=int(input())

    for idx in range(1,t+1):
        n,m=map(int,input().split())
        maps=[list(map(int,input().split()))for _ in range(n)]
        house=[]

        for r in range(n):
            for c in range(n):
                if maps[r][c]:
                    house.append((r,c))

        result=1

        for k in range(2,n+2):
            for r in range(n):
                for c in range(n):
                    cnt=0

                    for x,y in house:
                        if abs(r-x)+abs(c-y)<k:
                            cnt+=1

                    if cnt>result and cnt*m>=k**2+(k-1)**2:
                        result=cnt
        print("#{} {}".format(idx,result))