if __name__ == '__main__':
    i=1
    while True:
        l,p,v=map(int,input().split())

        if l==0 and p==0 and v==0:
            break
        res=0

        num1=v//p
        res+=num1*l

        tmp=v%p

        if tmp>l:
            res+=l
        else:
            res+=tmp
        print("Case %d: %d"%(i,res))
        i+=1