count=0
def printAllSubsetsRec(arr, n, v, sum) :
    global count  
    if (sum == 0) : 
        for value in range(len(v)) : 
            print(v[len(v)-value-1], end=" ")
        print(" ", end=" ")
        count +=1
        return 
    if (n == 0):
        return 
    printAllSubsetsRec(arr, n - 1, v, sum) 
    v1 = [] + v 
    v1.append(arr[n - 1]) 
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1]) 

def printAllSubsets(arr, n, sum): 
    v = [] 
    printAllSubsetsRec(arr, n, v, sum) 

n = int(input())
arr = []
if n!=0:
    for i in range(n):
        arr.append(int(input()))
    sum = int(input())
    printAllSubsets(arr, n, sum)
    print()
    print(count)