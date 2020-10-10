#고정점이란 수열의 원소 중에서 그값이 인덱스와 동일한 원소를 의미합니다.예를들어 수열 a={-15,-4,2,8,13}이 있을때 a[2]=2이므로 고정점은 2가 됩니다.


def binary_search(arr,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==mid:
        return mid
    elif arr[mid]>mid:
        return binary_search(arr,start,mid-1)
    else:
        return binary_search(arr,mid+1,end)

n=int(input())
arr=list(map(int,input().split()))
res=binary_search(arr,0,n-1)
print(res)