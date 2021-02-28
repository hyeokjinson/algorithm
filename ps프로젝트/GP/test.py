def main():
    def dfs(v):
        for x in graph[v]:
            res = ''
            if not visit[x]:
                res+=chr(x)
                visit[v] = True
                dfs(x)
                print(res)

    k = input().strip()

    n = int(input())

    graph = [[] * 150 for _ in range(150)]
    visit = [False] * 150
    for _ in range(n):
        a, b = map(str, input().split())
        graph[ord(a)].append(ord(b))

    dfs(ord(k[0]))


if __name__ == "__main__":
    main()