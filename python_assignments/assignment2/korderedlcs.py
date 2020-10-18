def lcs(n,m,a,b):
    arr=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(a[i]==b[j]):
                arr[i+1][j+1]=arr[i][j]+1
            else:
                arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
    return arr[-1][-1]

n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=m-len(b)
print(lcs(n,m,a,b)+k)