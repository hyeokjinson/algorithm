def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid=len(arr)//2
    l=h=0
    low=merge_sort(arr[:mid])
    high=merge_sort(arr[mid:])
    merge_arr=[]

    while l<len(low) and h<len(high):
        if low[l]<high[h]:
            merge_arr.append(low[l])
            l+=1
        else:
            merge_arr.append(high[h])
            h+=1
    if h==len(high):
        merge_arr+=low[l:]
    elif l==len(low):
        merge_arr+=high[h:]

    return merge_arr

if __name__ == '__main__':
    n=int(input())
    arr=[]

    for _ in range(n):
        arr.append(int(input()))

    arr=merge_sort(arr)

    for x in arr:
        print(x)