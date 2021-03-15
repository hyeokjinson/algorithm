바이너리 서치로 정답이 가능한 하위 문자열 길이 범위를 줄여나간다
legth를 문자열 길이의 하위 문자열이 문자열 S에 두번 이상 발생했는지 확인할때는 Rabin-Karp알고리즘을 사용한다.

라빈 카프 알고리즘은 해시 기법을 사용한다
문자열이 같은지 비교할 때 1차로 해시가 같은지 비교,해시가 같을때만 실제로 문자열이 같은지 비교

이런 해시값을 key값,문자열의 시작 인덱스 배열을 value값을 하는 map을 만든다




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
