def a_brute_force(l,w):
    if l>=len(a_weight):
        a_sum.append(w)
        return
    a_brute_force(l+1,w)
    a_brute_force(l+1,w+a_weight[l])

def b_brute_force(l,w):
    if l>=len(b_weight):
        b_sum.append(w)
        return
    b_brute_force(l+1,w)
    b_brute_force(l+1,w+b_weight[l])

def solve(start,end,res):

    while start<end:
        mid=(start+end)//2

        if b_sum[mid]<=res:
            start=mid+1
        else:
            end=mid
    return end

if __name__ == '__main__':
    n,c=map(int,input().split())

    arr=list(map(int,input().split()))

    a_weight=arr[:n//2]
    b_weight=arr[n//2:]

    a_sum=[]
    b_sum=[]

    a_brute_force(0,0)
    b_brute_force(0,0)
    cnt=0
    b_sum.sort()
    for i in a_sum:
        if c-i<0:
            continue
        cnt+=solve(0,len(b_sum),c-i)
    print(cnt)
