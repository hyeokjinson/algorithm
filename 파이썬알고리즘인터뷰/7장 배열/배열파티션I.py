def solve():
    res=0
    pair=[]
    nums.sort()
    for i in range(len(nums)):
        pair.append(nums[i])

        if len(pair)==2:
            res+=min(pair)
            pair=[]
    return res

def solve2():
    nums.sort()
    res=0
    for i,num in enumerate(nums):
        if i%2==0:
            res+=num
    return res

if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(solve())
    print(solve2())