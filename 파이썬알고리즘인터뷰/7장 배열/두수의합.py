def twosum():
    nums_map={}

    for i,num in enumerate(nums):
        nums_map[num]=i

    for i,num in enumerate(nums):
        if target-num in nums_map and i!=nums_map[target-num]:
            return [i,nums_map[target-num]]

def twosum1():
    left,right=0,len(nums)-1

    while not left==right:
        if nums[left]+nums[right]<target:
            left+=1
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            return [left,right]

if __name__ == '__main__':
    nums = [2,7,11,15]
    target=9

    print(twosum())
    print(twosum1())