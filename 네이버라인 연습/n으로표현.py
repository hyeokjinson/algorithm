def solution(N,number):
    answer=-1
    dp=[]
    for i in range(1,9):
        num_set={int(str(N)*i)}
        for j in range(0,i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    num_set.add(x+y)
                    num_set.add(x-y)
                    num_set.add(x*y)

                    if y!=0:
                        num_set.add(x//y)
        if number in num_set:
            return i
        dp.append(num_set)

    return answer

solution(5,12)
solution(2,11)