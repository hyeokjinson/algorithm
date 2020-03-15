n,m=map(int,input().split())
array=list(map(int,input().split()))
visit=[0 for i in range(n)]
result=0
def remove_values_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)

for i in range(m):
    if n//m==1 and n%m==0:
        result=0
        break
    elif m==1:
        result=max(array)-min(array)
        break
    else:
        for t in range(0,n):
            if len(array)-(m-1)==0:
                 break
            visit[t]=array.pop(0)
        remove_values_from_list(visit, 0)

        result = max(visit) - min(visit)
print(result)


