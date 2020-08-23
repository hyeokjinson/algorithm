import sys

def dfs(L,sum_):
    global res

    if L==0:
        res=True
    elif L<0:
        pass
    else:
        if sum_<3:
            for cnt in range(L//l_st[sum_],-1,-1):
                dfs(L-(l_st[sum_]*cnt),sum_+1)
                if res:
                    break


a,b,c,n=map(int,input().split())
l_st=[a,b,c]
l_st.sort(reverse=True)
res=False
dfs(n,0)
if res:
    print(1)
else:
    print(0)