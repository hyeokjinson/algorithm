def getPrimaryNum_Eratos(N):
    num=[True]*(N+1)
    for i in range(2,len(num)//2+1):
            for j in range(i+i,N,i):

                num[j]=False
    return [i for i in range(2,N) if num[i]==True]