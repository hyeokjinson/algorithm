class Solution:

    def longestDupSubstring(self, S='banana') -> str:
        def search(m, MOD):
            h = 0
            for i in range(m):
                h = (h * 26 + nums[i]) % MOD
            s = {h}
            aL = pow(26, m, MOD)
            for pos in range(1, n - m + 1):
                h = (h * 26 - nums[pos - 1] * aL + nums[pos + m - 1]) % MOD
                if h in s:
                    return pos
                s.add(h)
            return -1

        n = len(S)
        nums = [ord(c) - ord('a') for c in S]
        l, r = 1, n
        pos = -1
        MOD = 2**63 - 1
        while l <= r:
            m = (l + r) // 2
            cur = search(m, MOD)
            if cur != -1:
                l = m + 1
                pos = cur
            else:
                r = m - 1
        return S[pos: pos + l - 1]

#####################
def count(mid):
    h = 1
    cnt = 0

    for l in range(len(nums)):
        while h < len(nums) and nums[h] - nums[l] <= mid:
            h += 1
        cnt += max(0, (h - l - 1))
    return cnt


nums = list(map(int, input().split()))
k = int(input())

nums.sort()
rt = nums[-1] - nums[0]
lt = 0

while lt < rt:
    mid = (lt + rt) // 2
    cnt = count(mid)
    if cnt >= k:
        rt = mid
    else:
        lt = mid + 1

print(lt)
##################################
nums=list(map(int,input().split()))


n=len(nums)



jump,c1,c2=0,0,0

for i in range(n-1):
    c2=max(c2,i+nums[i])
    if i==c1:
        jump+=1
        c1=c2
print(jump)
