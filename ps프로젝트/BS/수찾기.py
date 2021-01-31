def solve(x):
    global start,end
    while start<=end:
        mid=(start+end)//2

        if a[mid]==x:
            return 1
        elif x>a[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))

    a.sort()
    res=[]


    for i in range(m):
        start = 0
        end = n - 1
        print(solve(b[i]))


