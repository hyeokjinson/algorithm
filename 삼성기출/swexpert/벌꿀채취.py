def getMaxSum(x,y,iter,sum_,profitAtSpot):
    if iter==m:
        if sum_<=c and maxProfit[y][x-m]<profitAtSpot:
            maxProfit[y][x-m]=profitAtSpot
    else:
        getMaxSum(x+1,y,iter+1,sum_,profitAtSpot)
        getMaxSum(x+1,y,iter+1,sum_+arr[y][x],profitAtSpot+arr[y][x]*arr[y][x])

def calcSumSpot():
    for i in range(n):
        for j in range(n-m+1):
            getMaxSum(j,i,0,0,0)

def solve():
    global max_value
    for i in range(n):
        for j in range(n-m+1):
            profit=maxProfit[i][j]

            for k in range(j+m,n-m+1):
                profit+=maxProfit[i][k]
                if profit>max_value:
                    max_value=profit
                profit-=maxProfit[i][k]

            for t in range(i+1,n):
                for k in range(n-m+1):
                    profit+=maxProfit[t][k]
                    if profit>max_value:
                        max_value=profit
                    profit-=maxProfit[t][k]

if __name__ == '__main__':
    t=int(input())

    for idx in range(1,t+1):
        n,m,c=map(int,input().split())
        arr=[list(map(int,input().split()))for _ in range(n)]
        maxProfit=[[0 for _ in range(n)]for _ in range(n)]
        max_value=-2147000000
        calcSumSpot()
        solve()
        print("#{} {}".format(idx,max_value))

# from itertools import combinations
# from functools import lru_cache
#
#
# @lru_cache()
# def cal_price(h):
#     return h ** 2
#
#
# def maxRow(y):
#     max_honey=0
#     for x in range(N - M + 1):
#         for rc in rowComb:
#             honey_sum=[]
#             break_flag=False
#             for c in rc:
#                 honey_sum.append(honeys[y][x + c])
#                 if sum(honey_sum) > C:
#                     break_flag=True
#                     break
#             if not break_flag:
#                 max_honey=max(max_honey, sum([cal_price(h) for h in honey_sum]))
#     return max_honey
#
#
# T=int(input())
# for tc in range(1, T + 1):
#     N, M, C=map(int, input().split())
#     honeys=[list(map(int, input().split())) for _ in range(N)]
#     rowComb=[c for m in range(1, M + 1) for c in combinations(range(M), m)]
#     result=[maxRow(y) for y in range(N)]
#     print("#%d %d" % (tc, sum(sorted(result)[-2:])))
