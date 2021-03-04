###########문제 1번

def solve(number, k):
    num = list(map(int, number))
    stack = []

    for x in num:
        while stack and k > 0 and stack[-1] > x:
            stack.pop()
            k -= 1
        stack.append(x)

    if k != 0:
        stack = stack[:-k]

    answer = ''.join(map(str, stack))
    return answer


num = input()
k = int(input())
res = solve(num, k)

if len(res) == 0:
    print(0)
else:
    print(int(res))

###################문제 2번
version1 = input()
version2 = input()

v1 = list(map(int, version1.split('.')))
v2 = list(map(int, version2.split('.')))

v1_value = 0
v2_value = 0

tmp = 1
for i in range(len(v1)):
    v1_value += tmp * v1[i]
    tmp = tmp * 0.1
tmp = 1
for i in range(len(v2)):
    v2_value += tmp * v2[i]
    tmp = tmp * 0.1

if v1_value < v2_value:
    print(-1)
elif v1_value > v2_value:
    print(1)
else:
    print(0)

############################문제3번
def solve(s):
    mod = 10 ** 9 + 7

    s1 = s.count('1')

    if s1 % 3:
        return 0
    s1 //= 3

    if s1 == 0:
        return (len(s) - 1) * (len(s) - 2) // 2 % mod

    cnt = lt = rt = 0

    for x in s:
        if x == '1':
            cnt += 1
        if cnt == s1:
            lt += 1
        elif cnt == 2 * s1:
            rt += 1
    return lt * rt % mod


s = input()

print(solve(s))

