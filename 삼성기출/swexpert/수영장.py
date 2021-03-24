def dfs(L,sum_):
    global min_

    if L>=12:
        if sum_<min_:
            min_=sum_
    else:
        dfs(L+1,sum_+costs[0]*plans[L])
        dfs(L+1,sum_+costs[1])
        dfs(L+3,sum_+costs[2])

if __name__ == '__main__':
    t=int(input())

    for i in range(1,t+1):
        costs=list(map(int,input().split()))
        plans=list(map(int,input().split()))
        min_=costs[-1]

        dfs(0,0)
        print("#{} {}".format(i,min_))
