def func(arr,x):
    res=0

    for i in range(len(arr)):
        res+=abs(i*x-arr[i])

    return int(res)

def solution():
    n=int(input())
    arr=list(map(int,input().split()))

    start=1
    end=1000000000

    while start+3<=end:
        lt=(2*start+end)//3
        rt=(start+2*end)//3

        w_l=func(arr,lt)
        w_r=func(arr,rt)

        if w_l<w_r:
            end=int(rt)
        else:
            start=int(lt)

    answer=2147000000

    for i in range(start,end+1):
        answer=min(answer,func(arr,i))
    print(answer)

if __name__ == '__main__':
    solution()