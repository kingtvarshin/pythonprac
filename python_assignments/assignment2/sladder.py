def board(M,N,ans):
    global count
    if(N==0):
        count = count + 1
        for x in ans:
            print(x,end="")
        return 
    for i in range(M):
        if (N-i-1) >= 0:
            ans.append(i+1)
            board(M,N-i-1,ans)
            ans.pop(len(ans)-1)
    print(" ",end="")

N = int(input())
M = int(input())
ans = []
count = 0
board(M,N,ans)
print()
print(count)
