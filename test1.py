# def solution(S):
#     if S not in 'a':
#         return 2 **len(S)
#     cnt=0
#     res=0
#     for i in range(len(S)):
#         if cnt>=3:
#             return -1
#         if S[i]=='a':
#             cnt+=1
#             continue
#         else:
#             if cnt<2:
#                 while cnt!=2:
#                     res+=1
#                     cnt+=1
#                 cnt=0
#
#     return res
#     pass

def solution(S):
    res = []
    for i in range(len(S) - 1):
        data = S[i]
        len_data = len(data)

        for j in range(i + 1, len(S)):
            data1 = S[j]
            for k in range(len_data):
                if S[i][k] == S[j][k]:
                    return [i, j, k]
    return []
S=["abc","bca","dbe"]
print(solution(S))