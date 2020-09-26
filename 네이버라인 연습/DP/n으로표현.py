def solution(N, number):
    answer = -1
    dp = []
    num_dic = set()
    for i in range(1, 9):
        num_dic.add(int(str(N)) * i)
        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    num_dic.add(x + y)
                    num_dic.add(x - y)
                    num_dic.add(x * y)
                    if y != 0:
                        num_dic.add(x // y)
        if number in num_dic:
            return i
        dp.append(num_dic)

    return answer
solution(5,12)