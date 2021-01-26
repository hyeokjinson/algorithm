from collections import deque


if __name__ == '__main__':
    n,t,g=map(int,input().split())
    MAX=100000



    if n==g:
        print(0)
    else:
        res = [-1]*(10**6)
        q = deque()
        q.append(n)
        res[n] =0
        flag = False
        while q:
            x=q.popleft()


            if res[x]>t:
                break

            if x==g:
                flag=True
                break

            temp=[x+1,x*2]

            for i in range(2):
                if temp[i]>99999:
                    continue
                if i and temp[i]:
                    temp[i]-=10**(len(str(temp[i]))-1)
                if res[temp[i]]==-1:
                    q.append(temp[i])
                    res[temp[i]]=res[x]+1

        if flag:
            print(res[g])
        else:
            print('ANG')