from itertools import product
# # def DFS(L,m,word_list):
# #     global cnt
# #     if L==m:
# #         for i in range(m):
# #             print(word_list[i], end=' ')
# #         print()
# #         cnt+=1
# #     else:
# #         for i in range(5):
# #             word_list[L]=word_list[i]
# #             DFS(L+1,m,word_list)
#
# def solution(word):
#     answer = 0
#     word_list=["A","E","I","O","U"]
#
#     for i in range(1,6):
#         result=list(product(word_list,repeat=i))
#         print(result)
#
#     return answer
#
# if __name__ == '__main__':
#     word=input()
#
#     print(solution(word))
import sys


def dfs(L):
    global cnt
    word_list = ["A", "E", "I", "O", "U"]

    print("res: ",res)
    if L ==5:
        for i in range(5):
            print(res[i], end=' ')
            cnt += 1
        print()

    else:
        print("else")
        for i in range(5):
            res[L]=word_list[i]
            dfs(L + 1)
if __name__ == '__main__':
    cnt=0
    res = [""] * 5
    dfs(0)
    print(cnt)


# def solution(word):
#     answer = 0
#     dfs(0)
#     return answer
# def DFS(L):
#     global cnt
#     if L==m:
#         for i in range(m):
#             print(res[i], end=' ')
#             cnt+=1
#         print()
#
#     else:
#         for i in range(1, n+1):
#             res[L]=i
#             DFS(L+1)
#
# if __name__=="__main__":
#     n, m=map(int, input().split())
#     res=[0]*n
#     cnt=0
#     DFS(0)
#     print(cnt)