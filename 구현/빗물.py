if __name__ == '__main__':
    h,w=map(int,input().split())
    height=list(map(int,input().split()))
    left,right=0,len(height)-1

    left_max=height[left]
    right_max=height[right]
    res=0
    while left<right:
        left_max=max(left_max,height[left])
        right_max=max(right_max,height[right])

        if left_max<=right_max:
            res+=left_max-height[left]
            left+=1
        else:
            res+=right_max-height[right]
            right-=1
    print(res)
