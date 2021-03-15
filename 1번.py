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