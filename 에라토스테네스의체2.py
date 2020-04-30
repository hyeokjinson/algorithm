N,K=map(int,input().split())
num=[True]*(N+1)
cnt=0
for i in range(2,len(num)+1):
        for j in range(i,N+1,i):
            if num[j] == True:
                num[j]=False
                cnt+=1
                if cnt==K:
                    print(j)
                    break
