
if __name__ == '__main__':
    n=int(input())
    c=[0]*1001

    arr=list(map(int,input().split()))

    arr=list(set(arr))
    arr.sort()
    print(*arr)