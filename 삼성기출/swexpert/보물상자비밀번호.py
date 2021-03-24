

if __name__ == '__main__':
    T=int(input())
    idx=1
    for _ in range(T):
        res=set()
        n,k=map(int,input().split())
        nums=list(input())
        leng=n//4

        for _ in range(leng):
            for i in range(4):
                res.add(''.join(nums[i*leng:(i+1)*leng]))
            nums.insert(0,nums.pop())
        result=[]
        for x in res:
            result.append(int(x,16))
        result.sort(reverse=True)
        print("#{} {}".format(idx,result[k-1]))
        idx+=1