import sys

input=sys.stdin.readline

def check1(x):
    s=str(x)
    res=False
    if len(s)==1:
        if int(s)%2==1:
            return True

    for i in range(1,len(s),2):
        if int(s[i])%2==0:
            res=True
        else:
            res=False
            break
    if res:
        return True
    else:
        return False
def check2(x):
    s = str(x)
    res=False
    for i in range(0,len(s),2):
        if int(s[i])%2==1:
            res=True
        else:
            res=False
            break
    if res:
        return True
    else:
        return False

if __name__ == '__main__':
    T=int(input())

    for i in range(T):
        l,r=map(int,input().split())
        cnt=0
        for x in range(l,r+1):
            if check1(x) and check2(x):
                cnt+=1
        print("Case #%d: %d" % (i+1, cnt))