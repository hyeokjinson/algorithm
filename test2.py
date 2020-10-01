A=[6,2,3,5,6,3]
B=[1,1,4,4]
C=[1,1,4,5,5,4]
# def dfs(x,dic):
#     cnt=0
#     if x not in dic:
#         cnt+=1
#         dfs(x+1,dic)
#         cnt-=1
#
#         cnt+=1
#         dfs(x-1,dic)
#         cnt-=1
#     return cnt
def solution(A):
    # write your code in Python 3.6
    dic={}
    cnt=0
    for x in A:
        if x not in dic:
            dic[x]=1
        else:
            if min(dic.keys())>=x:
                while True:
                    x+=1
                    cnt+=1
                    if x not in dic:
                        dic[x]=1
                        break
            elif min(dic.keys())<x:
                while True:
                    x-=1
                    cnt+=1
                    if x not in dic:
                        dic[x]=1
                        break
    return cnt
# def solution(A):
#     # write your code in Python 3.6
#     dic={}
#     cnt=0
#     for x in A:
#         if x not in dic:
#             dic[x]=1
#         else:
#             cnt+=dfs(x,dic)
#     return cnt
print(solution(A))
print(solution(B))