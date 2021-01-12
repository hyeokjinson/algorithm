import sys

input = sys.stdin.readline
if __name__ == '__main__':
    n, p = map(int, input().split())

    check = [[] for _ in range(n)]
    arr = []
    for _ in range(n):
        i, j = map(int, input().split())
        arr.append((i, j))
    cnt = 0
    for x, y in arr:
        if not check[x]:
            check[x].append(y)
            cnt += 1

        else:
            if y > check[x][-1]:
                check[x].append(y)
                cnt += 1
            elif y == check[x][-1]:
                continue
            else:
                while check[x] and y < check[x][-1]:
                    check[x].pop()
                    cnt += 1
                if check[x] and y == check[x][-1]:
                    continue
                check[x].append(y)
                cnt += 1
    print(cnt)


