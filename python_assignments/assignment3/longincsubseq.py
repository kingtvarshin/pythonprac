def lis(arr, n):
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if (arr[i]-1) not in s:
            j = arr[i]
            while(j in s):
                j+= 1
            ans = max(ans, j-arr[i])
    return ans

n = int(input())
sarr = input()
sarr = sarr.split()
arr = []
for i in sarr:
    arr.append(int(i))
print (lis(arr,n))