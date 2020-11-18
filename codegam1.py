def check(x,y):
    if x-y>y-1:
        return True
    else:
        return False
def sample1(n,k,s):
    res=0
    res+=k
    k=1
    for i in range(k,n+1):
        res+=1
    return res

def sample2(n,k,s):
    res=0
    res+=k-1
    while True:
        k-=1
        res+=1
        if k==s:
            for i in range(k,n+1):
                res+=1
            break
    return res

if __name__ == '__main__':
    T=int(input())

    for j in range(1,T+1):
        minute=0
        n,k,s=map(int,input().split())
        s1=sample1(n,k,s)
        s2=sample2(n,k,s)
        if s1>s2:
            print("case # %d : %d"%(j,s2))
        else:
            print("case # %d : %d" % (j, s1))
