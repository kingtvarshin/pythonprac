def printarray(a,n): 
    for x in range(n): 
        print(a[i] , " ",end="") 
    print()

def runCode(A,B,C,i,j,m,n,len,bool): 
    if (bool):
        if (len): 
            printarray(C, len+1) 
        for k in range(i,m): 
            if ( not len): 
                C[len] = A[k] 
                runCode(A, B, C, k+1, j, m, n, len,  not bool) 
            else:   
                if (A[k] > C[len]): 
                    C[len+1] = A[k] 
                    runCode(A, B, C, k+1, j, m, n, len+1, not bool) 
    else:   
        for l in range(j,n): 
            if (B[l] > C[len]): 
                C[len+1] = B[l] 
                runCode(A, B, C, i, l+1, m, n, len+1, not bool) 
              
def run(arr1,arr2,m,n): 
    arr3=[] 
    for i in range(m+n+1): 
        arr3.append(i) 
    runCode(arr1, arr2, arr3, 0, 0, m, n, 0, 1) 

a = input().split()
A = list(int(num) for num in input().split())
B = list(int(num) for num in input().split())
run(A, B, int(a[0]), int(a[1]))