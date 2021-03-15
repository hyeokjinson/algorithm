def solve(root,start,end):
    for i in range(start,end):
        if pre_order[root]==in_order[i]:
            solve(root+1,start,i)
            solve(root+i+1-start,i+1,end)
            print(pre_order[root],end=' ')

if __name__ == '__main__':
    T=int(input())

    for _ in range(T):
        n=int(input())
        pre_order=list(map(int,input().split()))
        in_order=list(map(int,input().split()))
        solve(0,0,n)
        print('')