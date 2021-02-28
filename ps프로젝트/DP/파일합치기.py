import heapq

def solve():
    for j in range(1,n):
        for i in range(j-1,-1,-1):
            min_=2147000000
            for k in range(j-i):
                min_=min(min_,dy[i][i+k]+dy[i+k+1][j])
            dy[i][j]=min_+sum(arr[i:j+1])

    print(dy[0][n-1])


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dy = [[0 for _ in range(n)] for _ in range(n)]
        solve()
