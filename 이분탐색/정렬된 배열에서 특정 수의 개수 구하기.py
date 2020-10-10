# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬 되어 있습니다 .이때 이 수열에서 x가 등장하는 횟수를 계산하세요
# ex)[1,1,2,2,2,2,3,]일때 x=2라면 2의 원소가 4개이므로 4를 출력
def first(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if (mid==0 or target>array[mid-1])and array[mid]==target:
        return mid
    elif array[mid]>=target:
        return first(array,target,start,mid-1)
    else:
        return first(array,target,mid+1,end)

def last(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if (mid==n-1 or target<arr[mid+1]) and array[mid]==target:
        return mid
    elif array[mid]>target:
        return last(array,target,start,mid-1)
    else:
        return last(array,target,mid+1,end)

def count_value(array,x):
    n=len(array)
    a=first(array,x,0,n-1)
    if a==None:
        return 0
    b=last(array,x,0,n-1)
    res=b-a+1
    return res


n,m=map(int,input().split())
arr=list(map(int,input().split()))
cnt=count_value(arr,m)
if cnt:
    print(cnt)
else:
    print(-1)