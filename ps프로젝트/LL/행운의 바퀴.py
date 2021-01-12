if __name__ == '__main__':
    n,k=map(int,input().split())
    board=['?']*n
    alpha_check=[False]*26
    word_stack=[]
    for _ in range(k):
        a,b=input().split()
        a=int(a)
        word_stack.append((a,b))

    i=0
    while word_stack:
        num,alpha=word_stack.pop()
        if board[i]=='?':
            if not alpha_check[ord(alpha)-ord('A')]:
                board[i]=alpha
                alpha_check[ord(alpha)-ord('A')]=True
            else:
                print('!')
                break
        else:
            if board[i]!=alpha:
                print('!')
                break
        i+=num
        i%=n
    else:
        print(''.join(board))